Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"

  config.vm.define "musicstreamer" do |musicstreamer|
    musicstreamer.vm.hostname = "musicstreamer"
    musicstreamer.vm.network "forwarded_port", guest: 8082, host: 8082

    musicstreamer.vm.provision "shell", path: ".provision/setup.sh"
  end
end
