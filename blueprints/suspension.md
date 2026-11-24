# Suspension

Fully active electromechanical suspension with passive springs in parallel, for the ScuderiaTroll car. All figures are design estimates for a fictional vehicle; masses and positions come from [weight-budget.md](weight-budget.md) and [layout.md](layout.md).

## Why Active

The car's downforce comes largely from a skirt-sealed floor and underfloor fans ([aero.md](aero.md)), which only work well if the floor stays at a steady height and attitude:

- **Varying aero load:** Total downforce swings from ~14 kN at 100 km/h to ~21 kN at 300 km/h, and the fan/wing mix changes with speed. Passive suspension would need very stiff springs to stop the car squatting at speed, hurting mechanical grip and kerb riding, and inviting porpoising.
- **Floor sealing:** Fan downforce depends on the skirt seal; ground-effect tunnels are sensitive to ride height and pitch. Active control holds both.
- **Tyres:** Better contact patch control and roll management help with the heavier car's tyre wear under the 3-swap cap (Sporting Rule 2).
- **Electrics already on board:** The high-voltage system powers electromechanical actuators directly, with energy recovery, and no hydraulic pump.

## Rules

- **Technical Rule 7:** Active suspension is explicitly permitted.
- **Automatic control only:** The suspension runs entirely from the car's operating state, with no driver-selectable modes, in line with Rule 7's automatic-control requirement for active aero. Control settings are fixed with the rest of the setup under parc fermé.
- **Technical Rule 2:** Hopping or launching the car has no benefit (no tyre contact means no grip), so the controller has no reason to do it. It may still raise ride height within its stroke (e.g. stalling the floor on straights to cut drag) or unload a single wheel over a kerb, since at least one wheel always stays on the track.

## Layout

Double wishbones at all four corners.

| | Front | Rear |
| --- | --- | --- |
| Actuation | Pushrod | Pullrod |
| Spring/actuator units | On top of the monocoque under the nose cover, clear of the front motors | Low on either side of the gearbox casing, below the LP turbo |
| Why | Keeps the units above the front MGU-Ks and driveshafts, which sit low either side of the footwell | Keeps mass low and leaves the top of the gearbox for the LP turbo and hydraulics |

**Front packaging (resolves a [layout.md](layout.md) open item):** With the spring/actuator units on top of the chassis, the space low in the front bulkhead is free for the front motors and their driveshafts. The driveshafts pass between the lower and upper wishbones, as on front-motor Le Mans prototypes; the pushrod runs ahead of the driveshaft.

## Corner Unit

Each corner has three elements working in parallel:

| Element | Job |
| --- | --- |
| **Coil spring** | Carries the car's static weight plus an average aero load, setting the nominal ride height. Keeps the car drivable if the actuator fails |
| **Electromechanical actuator** | Rotary motor driving a ball screw. Adds or removes force to hold the ride height and attitude as loads change |
| **Light passive damper** | Handles high-frequency inputs (kerb strikes, wheel hop at ~15–20 Hz) faster than the actuator can respond |

### Sizing

| Item | Value | Basis |
| --- | --- | --- |
| Static load per corner | ~2.4 kN | ~960 kg race-start mass / 4 |
| Peak aero load per corner | ~5.3 kN | ~21 kN capped downforce / 4 |
| Spring preload point | ~4.8 kN | Static + ~2.5 kN mid-range aero |
| **Actuator force** | **±4 kN peak** | Covers the swing from low-speed to capped downforce, plus braking and cornering transfer |
| Actuator stroke | ±40 mm | |
| Actuator bandwidth | ~10–15 Hz | The passive damper handles faster inputs |
| Power per corner | ~2 kW peak mechanical (4 kN × 0.5 m/s) | |
| **Total power** | **~1–3 kW average, ~8 kW peak**, partly recovered | From the high-voltage system |

### Materials

- **Wishbones and pushrods/pullrods:** Carbon-fibre composite.
- **Uprights, rockers, actuator housings, ball screws' nuts:** Alloy X.
- **Ball screws and bearings:** Steel (contact fatigue).
- **Actuator motors:** Copper windings, electrical-steel core, NdFeB magnets (legal under Rule 5).

## Control

| Function | What it does |
| --- | --- |
| **Platform hold** | Keeps floor height (~40 mm) and pitch within ~±5 mm as downforce and fuel load change, so the skirt seal and tunnels work consistently |
| **Roll control** | Replaces anti-roll bars; sets roll stiffness and front/rear load transfer per corner phase |
| **Pitch control** | Limits dive under braking and squat under acceleration |
| **Kerb and bump compliance** | Lets wheels follow kerbs while the body stays level; the passive dampers take the sharpest hits |
| **Tyre load management** | Smooths load peaks to reduce tyre wear |

**Inputs:** Laser ride-height sensors, underfloor pressure sensors (fan suction), wheel-load sensors, accelerometers, speed, steering angle, brake pressure, and throttle.

The suspension controller works with the fan controller ([aero.md](aero.md)): fan speed and platform height are set together, since skirt sealing depends on both.

## Failure Modes

| Failure | Result |
| --- | --- |
| One actuator fails | Its motor windings are short-circuited, turning it into a damper. The spring holds ride height; the car is drivable with reduced platform control |
| Controller or high-voltage loss | All four corners fall back to springs plus passive dampers and shorted-motor damping, like a stiff passive car. The driver can continue or pit |
| Spring breaks | Treated as damage under the normal repair rules (Sporting Rule 2) |

## Mass

| Item | Change (kg) |
| --- | --- |
| Four electromechanical actuators (~4.5 kg each) | +18 |
| Controller and wiring | +2 |
| Lighter coil springs and light dampers (replacing F1-style dampers and torsion bars) | −3 |
| Heave springs and anti-roll bars deleted | −5 |
| Rockers and mounts (net) | −2 |
| **Net** | **+10** |

Suspension rises from 50 kg to **60 kg**, and car + driver from ~847 kg to **~857 kg**. See [weight-budget.md](weight-budget.md).

## Open Items

1. **Geometry:** Wishbone pickup points, camber/caster/toe, anti-dive and anti-squat percentages need detailed kinematics work.
2. **Ride-height targets per circuit:** The ~40 mm floor height is a starting point; bumpy circuits may need more.
