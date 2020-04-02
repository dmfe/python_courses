from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ListBox Example")

        self.set_border_width(10)
        list_box = Gtk.ListBox()
        list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(list_box)

        # Checkbox
        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row_1.add(box_1)
        label = Gtk.Label("Check if you love cheeseburgers:")
        label.set_halign(Gtk.Align.START)
        check = Gtk.CheckButton()
        check.set_halign(Gtk.Align.END)
        box_1.pack_start(label, True, True, 0)
        box_1.pack_start(check, True, True, 0)
        list_box.add(row_1)

        # Toggle Switch
        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row_2.add(box_2)
        label = Gtk.Label("Burger making machine:")
        label.set_halign(Gtk.Align.START)
        switch = Gtk.Switch()
        switch.set_halign(Gtk.Align.END)
        box_2.pack_start(label, True, True, 0)
        box_2.pack_start(switch, True, True, 0)
        list_box.add(row_2)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

