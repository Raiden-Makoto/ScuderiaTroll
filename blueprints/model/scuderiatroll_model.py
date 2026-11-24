"""ScuderiaTroll ST67 primitive layout model.

Every component is a box or a cylinder, so the car can be rebuilt in Blender
or any other 3D tool. The component list below is the single source of truth
for the layout: masses match weight-budget.md and positions match layout.md.

Coordinates (metres, right-handed, Blender-compatible):
    x: rearward from the front axle centreline (rear axle at x = 3.5)
    y: toward the car's right side (exhaust side is left, i.e. negative y)
    z: up from the ground

Usage:
    In Blender:   Scripting workspace -> open this file -> Run Script
                  (or: blender --python scuderiatroll_model.py)
    Elsewhere:    python3 scuderiatroll_model.py
                  -> prints mass / CG report, writes scuderiatroll.obj/.mtl
                     and SVG previews next to this file.
"""

import math
import os

WHEELBASE = 3.5

# Colours (sRGB hex) per material key.
COLOURS = {
    "structure": "#3b4252",
    "bodywork": "#c8102e",
    "floor": "#2b2b2b",
    "aero": "#c8102e",
    "drs": "#ff6b81",
    "fan_car": "#00b894",
    "skirt": "#2d3436",
    "tyre": "#1a1a1a",
    "brake": "#8a8a8a",
    "suspension": "#5c5c5c",
    "actuator": "#e84393",
    "driver": "#f2c14e",
    "engine": "#d9822b",
    "gearbox": "#7a6a5a",
    "turbo": "#b0b0b0",
    "exhaust": "#a0522d",
    "aftertreatment": "#9fd3c7",
    "motor": "#2e86de",
    "inverter": "#54a0ff",
    "battery": "#10ac84",
    "hv": "#ff9f43",
    "cooling": "#74b9ff",
    "fan": "#636e72",
    "charge_air": "#81ecec",
    "fuel": "#fdcb6e",
    "def": "#dfe6e9",
    "electronics": "#6c5ce7",
    "hydraulics": "#e17055",
    "fire": "#d63031",
    "misc": "#636e72",
    "cg": "#ff00ff",
}


def box(name, group, mat, size, pos, mass, alpha=1.0, fluid=0.0):
    return dict(name=name, group=group, mat=mat, shape="box", size=size,
                pos=pos, mass=mass, alpha=alpha, fluid=fluid)


def cyl(name, group, mat, radius, length, axis, pos, mass, alpha=1.0, fluid=0.0):
    return dict(name=name, group=group, mat=mat, shape="cyl", radius=radius,
                length=length, axis=axis, pos=pos, mass=mass, alpha=alpha,
                fluid=fluid)


def point(name, group, pos, mass):
    return dict(name=name, group=group, mat="misc", shape="point", pos=pos,
                mass=mass, alpha=1.0, fluid=0.0)


# fmt: off
COMPONENTS = [
    # --- Chassis, aero & vehicle systems (453 kg) --------------------------
    box("Monocoque", "Chassis", "structure", (1.95, 0.75, 0.60), (0.875, 0, 0.36), 45, alpha=0.25),
    box("Halo_Pillar", "Chassis", "structure", (0.05, 0.05, 0.20), (0.95, 0, 0.72), 1),
    box("Halo_Hoop_L", "Chassis", "structure", (0.75, 0.04, 0.04), (1.35, -0.25, 0.80), 3),
    box("Halo_Hoop_R", "Chassis", "structure", (0.75, 0.04, 0.04), (1.35, 0.25, 0.80), 3),
    box("Nose_FrontCrash", "Chassis", "structure", (0.50, 0.25, 0.22), (-0.35, 0, 0.33), 8),
    box("RearCrash", "Chassis", "structure", (0.35, 0.20, 0.20), (3.92, 0, 0.30), 4),
    box("SideImpact_L", "Chassis", "structure", (0.40, 0.20, 0.08), (1.60, -0.50, 0.30), 1.5),
    box("SideImpact_R", "Chassis", "structure", (0.40, 0.20, 0.08), (1.60, 0.50, 0.30), 1.5),
    box("Floor", "Bodywork", "floor", (3.20, 1.40, 0.03), (2.00, 0, 0.055), 25),
    box("Sidepod_L", "Bodywork", "bodywork", (1.70, 0.40, 0.50), (2.30, -0.58, 0.32), 10, alpha=0.2),
    box("Sidepod_R", "Bodywork", "bodywork", (1.70, 0.40, 0.50), (2.30, 0.58, 0.32), 10, alpha=0.2),
    box("EngineCover", "Bodywork", "bodywork", (1.80, 0.50, 0.20), (2.75, 0, 0.55), 6, alpha=0.2),
    box("Airbox", "Bodywork", "bodywork", (0.40, 0.30, 0.30), (2.00, 0, 0.80), 4, alpha=0.25),
    box("FrontWing", "Aero", "aero", (0.28, 1.50, 0.10), (-0.75, 0, 0.12), 10),
    box("RearWing_MainPlane", "Aero", "aero", (0.35, 1.00, 0.12), (3.95, 0, 0.76), 4.5),
    box("RearWing_DRSFlap", "Aero", "drs", (0.20, 1.00, 0.05), (4.00, 0, 0.88), 2.5),
    cyl("UnderfloorFan_L", "Aero", "fan_car", 0.16, 0.20, "x", (3.85, -0.25, 0.22), 2.5),
    cyl("UnderfloorFan_R", "Aero", "fan_car", 0.16, 0.20, "x", (3.85, 0.25, 0.22), 2.5),
    box("UnderfloorFanDuct", "Aero", "fan_car", (0.25, 0.80, 0.06), (3.70, 0, 0.10), 4),
    box("Skirt_L", "Aero", "skirt", (2.60, 0.02, 0.06), (1.80, -0.70, 0.04), 4),
    box("Skirt_R", "Aero", "skirt", (2.60, 0.02, 0.06), (1.80, 0.70, 0.04), 4),
    box("BeamWing", "Aero", "aero", (0.20, 0.80, 0.06), (3.85, 0, 0.42), 2),
    box("RearWingPylon", "Aero", "aero", (0.10, 0.05, 0.35), (3.92, 0, 0.55), 2),
    box("Suspension_FL", "Suspension", "suspension", (0.25, 0.245, 0.20), (0, -0.4975, 0.32), 12.5),
    box("Suspension_FR", "Suspension", "suspension", (0.25, 0.245, 0.20), (0, 0.4975, 0.32), 12.5),
    box("Suspension_RL", "Suspension", "suspension", (0.25, 0.445, 0.20), (3.5, -0.3725, 0.32), 12.5),
    box("Suspension_RR", "Suspension", "suspension", (0.25, 0.445, 0.20), (3.5, 0.3725, 0.32), 12.5),
    box("ActiveUnit_FL", "Suspension", "actuator", (0.30, 0.08, 0.08), (0.25, -0.12, 0.62), 2.5),
    box("ActiveUnit_FR", "Suspension", "actuator", (0.30, 0.08, 0.08), (0.25, 0.12, 0.62), 2.5),
    box("ActiveUnit_RL", "Suspension", "actuator", (0.30, 0.08, 0.08), (3.30, -0.20, 0.18), 2.5),
    box("ActiveUnit_RR", "Suspension", "actuator", (0.30, 0.08, 0.08), (3.30, 0.20, 0.18), 2.5),
    cyl("Wheel_FL", "Wheels", "tyre", 0.36, 0.38, "y", (0, -0.81, 0.36), 20),
    cyl("Wheel_FR", "Wheels", "tyre", 0.36, 0.38, "y", (0, 0.81, 0.36), 20),
    cyl("Wheel_RL", "Wheels", "tyre", 0.36, 0.405, "y", (3.5, -0.7975, 0.36), 20.5),
    cyl("Wheel_RR", "Wheels", "tyre", 0.36, 0.405, "y", (3.5, 0.7975, 0.36), 20.5),
    cyl("Brake_FL", "Wheels", "brake", 0.16, 0.06, "y", (0, -0.72, 0.36), 8.5),
    cyl("Brake_FR", "Wheels", "brake", 0.16, 0.06, "y", (0, 0.72, 0.36), 8.5),
    cyl("Brake_RL", "Wheels", "brake", 0.15, 0.06, "y", (3.5, -0.70, 0.36), 6),
    cyl("Brake_RR", "Wheels", "brake", 0.15, 0.06, "y", (3.5, 0.70, 0.36), 6),
    cyl("SteeringRack", "Chassis", "misc", 0.03, 0.50, "y", (0.10, 0, 0.45), 6),
    cyl("SteeringWheel", "Chassis", "misc", 0.14, 0.04, "x", (1.00, 0, 0.55), 4),
    box("Electronics_L", "Systems", "electronics", (0.30, 0.25, 0.15), (1.60, -0.52, 0.20), 15),
    box("Electronics_R", "Systems", "electronics", (0.30, 0.25, 0.15), (1.60, 0.52, 0.20), 15),
    box("Radiator_L", "Cooling", "cooling", (0.50, 0.30, 0.35), (2.00, -0.60, 0.30), 20),
    box("Radiator_R", "Cooling", "cooling", (0.50, 0.30, 0.35), (2.00, 0.60, 0.30), 20),
    box("RadiatorFanDuct_L", "Cooling", "fan", (1.30, 0.10, 0.10), (2.95, -0.55, 0.13), 0.5),
    box("RadiatorFanDuct_R", "Cooling", "fan", (1.30, 0.10, 0.10), (2.95, 0.55, 0.13), 0.5),
    box("Hydraulics", "Systems", "hydraulics", (0.25, 0.20, 0.15), (3.00, 0, 0.50), 12),
    cyl("FireExtinguisher", "Systems", "fire", 0.06, 0.30, "x", (0.55, 0, 0.12), 5),
    box("FuelCell", "Systems", "fuel", (0.55, 0.75, 0.50), (2.125, 0, 0.36), 12, alpha=0.5, fluid=94),
    box("Mirror_L", "Chassis", "misc", (0.12, 0.05, 0.08), (0.90, -0.48, 0.66), 1),
    box("Mirror_R", "Chassis", "misc", (0.12, 0.05, 0.08), (0.90, 0.48, 0.66), 1),
    point("Misc_Fasteners_Paint_Cameras", "Chassis", (1.80, 0, 0.40), 11),

    # --- Driver (80 kg) ------------------------------------------------------
    box("Driver_Legs", "Driver", "driver", (0.95, 0.35, 0.20), (0.70, 0, 0.28), 25),
    box("Driver_Torso", "Driver", "driver", (0.50, 0.45, 0.32), (1.45, 0, 0.36), 48),
    box("Driver_Head", "Driver", "driver", (0.28, 0.25, 0.28), (1.65, 0, 0.64), 7),

    # --- Powertrain (329 kg) ---------------------------------------------------
    box("Engine_OP4", "Powertrain", "engine", (0.50, 0.80, 0.35), (2.65, 0, 0.245), 109),
    box("Gearbox", "Powertrain", "gearbox", (0.75, 0.30, 0.25), (3.35, 0, 0.25), 45),
    cyl("MGUK_Rear", "Electric", "motor", 0.09, 0.22, "x", (3.05, 0.25, 0.22), 18),
    box("ExhaustManifold", "Powertrain", "exhaust", (0.45, 0.08, 0.12), (2.65, -0.44, 0.25), 5),
    cyl("Turbo_HP", "Powertrain", "turbo", 0.10, 0.25, "x", (2.75, -0.60, 0.33), 10),
    cyl("Aftertreatment", "Powertrain", "aftertreatment", 0.11, 0.42, "x", (3.10, -0.50, 0.30), 14),
    cyl("Turbo_LP", "Powertrain", "turbo", 0.11, 0.25, "x", (3.35, -0.28, 0.52), 11),
    box("ChargeAirCooler_1", "Cooling", "charge_air", (0.25, 0.15, 0.20), (2.75, 0.56, 0.32), 7.5),
    box("ChargeAirCooler_2", "Cooling", "charge_air", (0.25, 0.15, 0.20), (3.02, 0.56, 0.32), 7.5),
    box("DEF_Tank", "Powertrain", "def", (0.20, 0.15, 0.15), (3.25, 0.45, 0.25), 0, fluid=4),
    box("Inverter_Rear", "Electric", "inverter", (0.20, 0.15, 0.08), (2.95, 0.30, 0.45), 4),
    cyl("MGUK_Front_L", "Electric", "motor", 0.08, 0.20, "y", (0.15, -0.27, 0.30), 14),
    cyl("MGUK_Front_R", "Electric", "motor", 0.08, 0.20, "y", (0.15, 0.27, 0.30), 14),
    cyl("Driveshaft_FL", "Electric", "suspension", 0.025, 0.25, "y", (0.07, -0.495, 0.32), 3),
    cyl("Driveshaft_FR", "Electric", "suspension", 0.025, 0.25, "y", (0.07, 0.495, 0.32), 3),
    box("HV_Cable_Front", "Electric", "hv", (1.60, 0.03, 0.03), (1.10, 0.30, 0.10), 3),
    box("HV_Cable_Rear", "Electric", "hv", (1.00, 0.03, 0.03), (2.40, 0.30, 0.09), 3),
    box("Battery", "Electric", "battery", (0.60, 0.50, 0.12), (1.50, 0, 0.12), 50),
    box("BatteryCoolingCore", "Cooling", "cooling", (0.15, 0.25, 0.20), (2.10, 0, 0.72), 8),
]
# fmt: on


# ---------------------------------------------------------------------------
# Mass properties
# ---------------------------------------------------------------------------

def mass_properties(include_fluids):
    m = sx = sy = sz = 0.0
    for c in COMPONENTS:
        cm = c["mass"] + (c["fluid"] if include_fluids else 0.0)
        x, y, z = c["pos"]
        m += cm
        sx += cm * x
        sy += cm * y
        sz += cm * z
    return m, (sx / m, sy / m, sz / m)


def report():
    lines = []
    groups = {}
    for c in COMPONENTS:
        groups[c["group"]] = groups.get(c["group"], 0.0) + c["mass"]
    lines.append("Mass by group (dry, kg):")
    for g, gm in groups.items():
        lines.append(f"  {g:<12} {gm:7.1f}")
    for label, fluids in (("Car + driver (no fuel/DEF)", False), ("Race start", True)):
        m, (x, y, z) = mass_properties(fluids)
        front = (WHEELBASE - x) / WHEELBASE * 100
        lines.append(f"{label}: {m:.1f} kg")
        lines.append(f"  CG x = {x:.3f} m behind front axle -> front/rear = {front:.1f} / {100 - front:.1f}")
        lines.append(f"  CG z = {z:.3f} m, CG y = {y * 1000:+.1f} mm ({'right' if y > 0 else 'left'})")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Geometry (shared by OBJ and SVG export)
# ---------------------------------------------------------------------------

CYL_SEGMENTS = 24


def _axis_frame(axis):
    # Returns a function mapping local (u, v, w) -> world, with w along the axis
    # and (u, v, w) right-handed.
    if axis == "x":
        return lambda u, v, w: (w, u, v)
    if axis == "y":
        return lambda u, v, w: (v, w, u)
    return lambda u, v, w: (u, v, w)


def mesh(c):
    """Return (vertices, faces) for a component; faces are CCW from outside."""
    px, py, pz = c["pos"]
    if c["shape"] == "box":
        a, b, h = (s / 2 for s in c["size"])
        verts = [(px + (a if i else -a), py + (b if j else -b), pz + (h if k else -h))
                 for i in (0, 1) for j in (0, 1) for k in (0, 1)]
        idx = lambda i, j, k: i * 4 + j * 2 + k
        faces = [
            [idx(0, 0, 0), idx(0, 0, 1), idx(0, 1, 1), idx(0, 1, 0)],  # -x
            [idx(1, 0, 0), idx(1, 1, 0), idx(1, 1, 1), idx(1, 0, 1)],  # +x
            [idx(0, 0, 0), idx(1, 0, 0), idx(1, 0, 1), idx(0, 0, 1)],  # -y
            [idx(0, 1, 0), idx(0, 1, 1), idx(1, 1, 1), idx(1, 1, 0)],  # +y
            [idx(0, 0, 0), idx(0, 1, 0), idx(1, 1, 0), idx(1, 0, 0)],  # -z
            [idx(0, 0, 1), idx(1, 0, 1), idx(1, 1, 1), idx(0, 1, 1)],  # +z
        ]
        return verts, faces
    if c["shape"] == "cyl":
        to_world = _axis_frame(c["axis"])
        r, half, n = c["radius"], c["length"] / 2, CYL_SEGMENTS
        verts = []
        for w in (-half, half):
            for i in range(n):
                t = 2 * math.pi * i / n
                lx, ly, lz = to_world(r * math.cos(t), r * math.sin(t), w)
                verts.append((px + lx, py + ly, pz + lz))
        faces = [[i, (i + 1) % n, n + (i + 1) % n, n + i] for i in range(n)]
        faces.append([n + i for i in range(n)])          # +w cap
        faces.append([i for i in reversed(range(n))])     # -w cap
        return verts, faces
    return [], []


def cg_marker():
    m, cg = mass_properties(False)
    return box("CG_marker", "Reference", "cg", (0.06, 0.06, 0.06), cg, 0)


# ---------------------------------------------------------------------------
# OBJ export
# ---------------------------------------------------------------------------

def _hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def export_obj(obj_path):
    mtl_path = os.path.splitext(obj_path)[0] + ".mtl"
    with open(mtl_path, "w") as f:
        f.write("# ScuderiaTroll materials\n")
        for key, hexcol in COLOURS.items():
            r, g, b = _hex_to_rgb(hexcol)
            alpha = min((c["alpha"] for c in COMPONENTS if c["mat"] == key), default=1.0)
            f.write(f"newmtl {key}\nKd {r:.4f} {g:.4f} {b:.4f}\nd {alpha:.2f}\n\n")
    offset = 1
    with open(obj_path, "w") as f:
        f.write("# ScuderiaTroll primitive layout model (metres; x rearward, y right, z up)\n")
        f.write(f"mtllib {os.path.basename(mtl_path)}\n")
        for c in COMPONENTS + [cg_marker()]:
            verts, faces = mesh(c)
            if not verts:
                continue
            f.write(f"o {c['name']}\nusemtl {c['mat']}\n")
            for v in verts:
                f.write("v {:.4f} {:.4f} {:.4f}\n".format(*v))
            for face in faces:
                f.write("f " + " ".join(str(offset + i) for i in face) + "\n")
            offset += len(verts)


# ---------------------------------------------------------------------------
# SVG previews (painter's algorithm, flat shading)
# ---------------------------------------------------------------------------

def _sub(a, b): return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
def _dot(a, b): return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def _cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def _norm(a):
    length = math.sqrt(_dot(a, a)) or 1.0
    return (a[0] / length, a[1] / length, a[2] / length)


def _camera(forward, up_hint=(0, 0, 1)):
    fwd = _norm(forward)
    right = _norm(_cross(fwd, up_hint))
    up = _cross(right, fwd)
    return fwd, right, up


VIEWS = {
    # name: (forward direction, up hint, title)
    "iso": ((0.75, 0.85, -0.65), (0, 0, 1), "Isometric (front-left, from above)"),
    "top": ((0, 0, -1), (-1, 0, 0), "Top view"),
    "side": ((0, 1, 0), (0, 0, 1), "Side view (left / exhaust side)"),
    "front": ((1, 0, 0), (0, 0, 1), "Front view"),
}


def _shade(hexcol, factor):
    r, g, b = _hex_to_rgb(hexcol)
    return "#{:02x}{:02x}{:02x}".format(*(int(max(0, min(1, ch * factor)) * 255) for ch in (r, g, b)))


def export_svg(svg_path, view, width=1100, height=640):
    fwd, right, up = _camera(VIEWS[view][0], VIEWS[view][1])
    if view == "top":
        right, up = (1, 0, 0), (0, -1, 0)
    light = _norm((-0.4, -0.6, 1.0))
    polys = []
    for c in COMPONENTS + [cg_marker()]:
        verts, faces = mesh(c)
        for face in faces:
            pts = [verts[i] for i in face]
            normal = _norm(_cross(_sub(pts[1], pts[0]), _sub(pts[2], pts[0])))
            if _dot(normal, fwd) >= 0:
                continue
            centroid = tuple(sum(p[k] for p in pts) / len(pts) for k in range(3))
            depth = _dot(centroid, fwd)
            shade = 0.55 + 0.45 * max(0.0, _dot(normal, light))
            proj = [(_dot(p, right), _dot(p, up)) for p in pts]
            polys.append((depth, proj, _shade(COLOURS[c["mat"]], shade), c["alpha"]))
    xs = [p[0] for _, proj, _, _ in polys for p in proj]
    ys = [p[1] for _, proj, _, _ in polys for p in proj]
    margin = 60
    scale = min((width - 2 * margin) / (max(xs) - min(xs)), (height - 2 * margin - 40) / (max(ys) - min(ys)))
    ox = margin - min(xs) * scale + ((width - 2 * margin) - (max(xs) - min(xs)) * scale) / 2
    oy = margin + 40 + max(ys) * scale
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
           f'<rect width="{width}" height="{height}" fill="#f7f7f5"/>',
           f'<text x="{margin}" y="40" font-family="sans-serif" font-size="22" fill="#222">ScuderiaTroll ST67: {VIEWS[view][2]}</text>']
    for depth, proj, colour, alpha in sorted(polys, key=lambda p: -p[0]):
        pts = " ".join(f"{ox + px * scale:.1f},{oy - py * scale:.1f}" for px, py in proj)
        stroke_op = 0.35 if alpha < 1 else 0.6
        out.append(f'<polygon points="{pts}" fill="{colour}" fill-opacity="{alpha}" '
                   f'stroke="#222" stroke-opacity="{stroke_op}" stroke-width="0.6"/>')
    # 1 m scale bar
    sx, sy = margin, height - 30
    out.append(f'<line x1="{sx}" y1="{sy}" x2="{sx + scale}" y2="{sy}" stroke="#222" stroke-width="3"/>')
    out.append(f'<text x="{sx + scale + 8}" y="{sy + 5}" font-family="sans-serif" font-size="14" fill="#222">1 m</text>')
    if view in ("top", "side"):
        out.append(f'<text x="{width - margin}" y="{sy + 5}" font-family="sans-serif" font-size="14" '
                   f'fill="#222" text-anchor="end">front ← → rear</text>')
    if view == "top":
        out.append(f'<text x="{width - margin}" y="40" font-family="sans-serif" font-size="14" '
                   f'fill="#222" text-anchor="end">top edge: left (exhaust) side · bottom edge: right (intake) side</text>')
    out.append("</svg>")
    with open(svg_path, "w") as f:
        f.write("\n".join(out))


# ---------------------------------------------------------------------------
# Blender build
# ---------------------------------------------------------------------------

def build_blender():
    import bpy

    root = bpy.data.collections.get("ScuderiaTroll") or bpy.data.collections.new("ScuderiaTroll")
    if root.name not in bpy.context.scene.collection.children:
        bpy.context.scene.collection.children.link(root)

    materials = {}

    def material(key, alpha):
        name = f"ST_{key}"
        if name in materials:
            return materials[name]
        mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        r, g, b = _hex_to_rgb(COLOURS[key])
        if bsdf:
            bsdf.inputs["Base Color"].default_value = (r, g, b, 1.0)
            bsdf.inputs["Alpha"].default_value = alpha
        mat.diffuse_color = (r, g, b, alpha)
        if alpha < 1:
            if hasattr(mat, "surface_render_method"):
                mat.surface_render_method = "BLENDED"
            elif hasattr(mat, "blend_method"):
                mat.blend_method = "BLEND"
        materials[name] = mat
        return mat

    def collection(group):
        name = f"ST_{group}"
        col = bpy.data.collections.get(name)
        if col is None:
            col = bpy.data.collections.new(name)
            root.children.link(col)
        return col

    for c in COMPONENTS + [cg_marker()]:
        if c["shape"] == "point":
            obj = bpy.data.objects.new(c["name"], None)
            obj.empty_display_type = "SPHERE"
            obj.empty_display_size = 0.05
            obj.location = c["pos"]
        else:
            verts, faces = mesh(c)
            me = bpy.data.meshes.new(c["name"])
            me.from_pydata(verts, [], faces)
            me.update()
            obj = bpy.data.objects.new(c["name"], me)
            obj.data.materials.append(material(c["mat"], c["alpha"]))
        obj["mass_kg"] = c["mass"]
        if c["fluid"]:
            obj["fluid_kg"] = c["fluid"]
        collection(c["group"]).objects.link(obj)


# ---------------------------------------------------------------------------

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    print(report())
    export_obj(os.path.join(here, "scuderiatroll.obj"))
    for view in VIEWS:
        export_svg(os.path.join(here, f"preview_{view}.svg"), view)
    print(f"Wrote scuderiatroll.obj/.mtl and preview_*.svg to {here}")


try:
    import bpy  # noqa: F401
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

if __name__ == "__main__":
    if IN_BLENDER:
        build_blender()
    else:
        main()
