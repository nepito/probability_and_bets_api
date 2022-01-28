resource "digitalocean_droplet" "web" {
	image = "ubuntu-20-04-x64"
	name = "predictions"
	region = "SFO3"
	size = "s-1vcpu-1gb"
	user_data = "${file("userdata.yaml")}"
	ssh_keys = ["${digitalocean_ssh_key.nepito.fingerprint}"]
}