resource "digitalocean_ssh_key" "nepito" {
	name = "nepolin"
	public_key = "${file("~/.ssh/id_rsa.pub")}"
}