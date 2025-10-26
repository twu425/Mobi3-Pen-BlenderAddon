# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import sys, subprocess, ensurepip
import bpy

def ensure_hidapi():
    try:
        import hid
    except ImportError:
        ensurepip.bootstrap()
        subprocess.check_call([sys.executable, "-m", "pip", "install", "hidapi"])

def register():
    ensure_hidapi()
    import hid
    VID = 0x239A  
    PID = 0x80F4  

    device = hid.device()
    device.open(VID, PID)

def unregister(): ...


def create_grease_pencil(name="GPencil"):
    # Create grease pencil object if not exists
    if name in bpy.data.objects:
        return bpy.data.objects[name]
    
    gp_data = bpy.data.grease_pencils.new(name)
    gp_obj = bpy.data.objects.new(name, gp_data)
    bpy.context.collection.objects.link(gp_obj)
    bpy.context.view_layer.objects.active = gp_obj
    return gp_obj