import gi, subprocess, re, platform
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

class Info():
    def get_distro():
        with open('/usr/lib/os-release') as tmp:
            dump = tmp.read()
        distro_name = re.search("PRETTY_NAME=\"(.*?)\"", dump).group(1)
        try:
            distro_release = re.search("BUILD_ID=(.*?)\n", dump).group(1)
        except:
            distro_release = re.search("VERSION=(.*?)\n", dump).group(1)
        distro = distro_name + "\n              Version: " + distro_release
        return distro
    
    def get_logo():
        logo_pixbuf = GdkPixbuf.Pixbuf.new_from_file("logo.png")
        logo_pixbuf = logo_pixbuf.scale_simple(logo_pixbuf.get_width() * 0.5, logo_pixbuf.get_height() * 0.5, GdkPixbuf.InterpType.BILINEAR)
        logo = Gtk.Image.new_from_pixbuf(logo_pixbuf)
        return logo

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("About this distro")
        self.set_default_size(460, 390)
        self.set_resizable(False)
        self.set_position(1)
        
        distro_logo = Info.get_logo()
        label_distro = Gtk.Label("              Distribution: " + Info.get_distro())
        label_distro.set_halign(1)
        label_kernel = Gtk.Label("              Kernel version: " + platform.uname()[2] + "\n              Kernel type: " + platform.uname()[0])
        label_kernel.set_halign(1)

        box = Gtk.VBox(False)
        box.pack_start(distro_logo, False, False, 20)
        box.pack_start(label_distro, False, False, 1)
        box.pack_start(label_kernel, False, False, 1)

        self.add(box)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
