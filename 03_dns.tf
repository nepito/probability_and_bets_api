resource "digitalocean_domain" "macer" {
	name = "macer.tech"
}

resource "digitalocean_record" "www" {
	domain = digitalocean_domain.macer.id
	type = "A"
	name = "nies"
	value = "${digitalocean_droplet.web.ipv4_address}"
}
