Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"

  config.vm.define "streamer" do |streamer|
    streamer.vm.hostname = "streamer"
    streamer.vm.network "forwarded_port", guest: 8082, host: 8082

    streamer.vm.provision "shell", path: ".provision/setup.sh"
  end
end
