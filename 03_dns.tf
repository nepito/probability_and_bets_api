resource "digitalocean_domain" "macer" {
	name = "nies.macer.tech"
}

resource "digitalocean_record" "www" {
	domain = digitalocean_domain.macer.id
	type = "A"
	name = "www"
	value = "${digitalocean_droplet.web.ipv4_address}"
}
