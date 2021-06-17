import gi
gi.require_version("Wnck", "3.0")
from gi.repository import Wnck
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, Gtk
from gi.repository import GdkX11,GdkPixbuf
import time
import cv2
import numpy
from PIL import Image

class screensoter:
    def __init__(self, win_name):
        """init self and find correct window"""
        w=None
        print("Searching for %s window..." %win_name)
        while w is None:
            scr = Wnck.Screen.get_default()
            scr.force_update()
            w = next((x for x in scr.get_windows() if win_name in x.get_name()), None) #find window with the name of win_name argument

        Gdk.Window.process_all_updates()
        xlib_window = w.get_xid() # get xid of the window to take screenshots from as X11 display
        gdk_display = GdkX11.X11Display.get_default()
        self.gdk_window = GdkX11.X11Window.foreign_new_for_display(gdk_display, xlib_window)
        print("Window Found! Ready to take screenshots!")

    def get_screenshot(self):
        """take screenshot"""
        pb = Gdk.pixbuf_get_from_window(self.gdk_window, *self.gdk_window.get_geometry())
        img = screensoter.pixbuf2image(pb)
        open_cv_image = numpy.array(img) 
        return open_cv_image[:, :, ::-1].copy()

    def pixbuf2image(pix):
        """Convert gdkpixbuf to PIL image"""
        data = pix.get_pixels()
        w = pix.props.width
        h = pix.props.height
        stride = pix.props.rowstride
        mode = "RGB"
        if pix.props.has_alpha == True:
            mode = "RGBA"
        im = Image.frombytes(mode, (w, h), data, "raw", mode, stride)
        return im