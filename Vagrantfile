Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"

  config.vm.define "ninetwentysix" do |ninetwentysix|
    ninetwentysix.vm.hostname = "ninetwentysix"
    ninetwentysix.vm.network "forwarded_port", guest: 8082, host: 8082

    ninetwentysix.vm.provision "shell", path: ".provision/setup.sh"
  end
end
