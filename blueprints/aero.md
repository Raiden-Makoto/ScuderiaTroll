# Aerodynamics

Aero concept for the ScuderiaTroll ST67: a fan-assisted ground-effect car in the spirit of the Brabham BT46B, with sliding skirts, smaller wings than a pure wing car, fully automatic active aero, and DRS as the only driver-operated aero device.

All figures are design estimates for a fictional vehicle. Mass and layout come from [weight-budget.md](weight-budget.md) and [layout.md](layout.md).

## Rules That Apply

- **Technical Rule 7:** Fan cars, sliding skirts, and active aero are legal. Movable aero must be automatic (car-state-controlled), except DRS. The rear wing's drag-reduction element may only open through DRS.
- **Sporting Rule 16 (DRS):** Designated zones only, within 1 s of the car ahead at the detection point; closes under braking; disabled for 2 laps after the start and Safety Car restarts, and when Race Control deems it unsafe.
- **Technical Rule 2:** At least one wheel on the ground. Fan suction pulls the car down, so it's fully compatible.
- **Technical Rule 3:** Everything fits within 5.5 × 2.0 × 1.2 m; the rear wing tops out at ~0.95 m.

## Concept

Three downforce sources, blended by the active aero controller:

| Source | How it works | Varies with speed? | Drag |
| --- | --- | --- | --- |
| **Underfloor fan** | Two electric fans at the rear suck air out from under the skirt-sealed floor, lowering its pressure | **No:** full suction even at walking pace | Almost none; costs electrical power instead |
| **Ground-effect tunnels & diffuser** | Venturi tunnels under the sidepods accelerate air under the floor, exiting through the rear diffuser | Yes (∝ speed²) | Low |
| **Wings** | Front wing and rear wing (with DRS flap), smaller than an F1 car's because the fan does much of the work | Yes (∝ speed²) | Highest per unit of downforce |

Because the fan's downforce doesn't depend on speed and costs almost no drag, the car carries **F1-beating grip in slow and medium corners**, and can run **smaller, lower-drag wings** for the same high-speed grip.

## Underfloor Fan System

### Sealed Floor

| Item | Value |
| --- | --- |
| Sealed area (between skirts, x ≈ 0.5–3.1 m, ~1.2 m wide) | ~3.0 m² |
| Seal perimeter (side skirts plus front lip and rear fan duct) | ~7.6 m |
| Design underfloor suction | ~4.0 kPa (40 mbar) below ambient |
| **Fan downforce at design suction** | **~12 kN** (≈1.3× the car's race-start weight) |
| Maximum | ~14 kN at ~4.7 kPa |

### Fans

- **Two lightweight axial fans**, ~0.32 m diameter, one either side of the gearbox behind the rear axle, exhausting rearward through the diffuser. Carbon-composite blades and compact high-speed motors keep each fan unit (motor, rotor, inverter) to ~2.5 kg; at 12.5 kW each, they don't need heavy-duty hardware.
- **Airflow:** With an average skirt gap of ~5 mm, leakage into the floor is ~1.9 m³/s at 40 mbar.
- **Power:** ~11 kW of air power at design suction. Each fan has a 12.5 kW electric motor (25 kW total), leaving headroom for skirt lift over kerbs and bumps, and for radiator airflow at low speed (below).
- **Speed:** ~5,800 RPM fan speed (~100 m/s blade-tip speed).
- **Power source:** The high-voltage system (battery, MGU-H, or the MGU-Ks generating from the diesel). Averaged over a lap the fans draw ~15 kW, which costs ~4 kg of extra fuel per race (see [powertrain.md](powertrain.md) M4).
- **Debris guard:** Mesh at the fan exits and an upward-angled exhaust, so the fans don't fire gravel and debris at following cars (the BT46B's biggest complaint from rivals). Debris guards are **safety parts** (Sporting Rule 5): they can be replaced as often as needed without penalty.

### Fan Materials

| Part | Material | Why |
| --- | --- | --- |
| Blades | Carbon-fibre composite | Light and stiff; blade loads at ~100 m/s tip speed are modest |
| Blade leading edges | Thin Alloy X sheaths | The fans ingest grit, sand, and rubber from under the floor; metal-sheathed carbon blades are standard on modern jet-engine fans |
| Hub | Alloy X | Strong, light, holds the blade roots |
| Shroud & duct | Carbon-fibre composite | Light; the hottest air (radiator exit, ~60–80 °C) is well within epoxy limits |
| Inlet screen & exit debris guard | Alloy X mesh | Inlet screen keeps gravel off the blades; exit guard protects following cars. Both fit within the 4 kg duct and guard allowance |
| Motor housing | Alloy X | |
| Motor internals | Copper windings, electrical-steel core, NdFeB permanent magnets | Standard high-power-density motor materials. Rare-earth magnets are legal under Rule 5: export licensing isn't a ban while supply remains available |

### Shared Cooling Duty

Like the BT46B, the fans also cool the car. Ducts run from the sidepod radiator exits to the fan plenum:

- **At low speed** (Safety Car, pit lane, grid, slow corners), a valve in each duct opens and the fans pull air through the radiators as well as from under the floor. Rejecting ~70 kW at low speed takes ~1.5 m³/s of radiator airflow, adding ~9 kW of fan power (~20 kW total, within the 25 kW rating).
- **At high speed**, ram air cools the radiators and the valves close, so the fans work only on the floor.
- This **deletes the two separate cooling fans** from [cooling.md](cooling.md).

### Sliding Skirts

- **Vertical carbon-composite blades** in channels along the lower edge of each sidepod, running from just behind the front wheels to just ahead of the rear wheels.
- **Spring-loaded** to stay in light contact with the track, and pulled down further by the underfloor suction.
- **Replaceable ceramic-composite wear strips** on the bottom edge. These are **not** safety parts. Fresh strips are fitted before every race (free, within standard FIA parc fermé rules, so in practice before qualifying or as an approved like-for-like replacement); replacing worn strips mid-race uses one of the 3 swaps (Sporting Rule 2), so teams would combine it with a tyre stop, where the same swap covers both.
- **Front seal:** A flexible lip at the front of the floor. **Rear seal:** The fan duct and diffuser.

## Downforce Schedule

The active aero controller sets fan speed and front wing flap angle from the car's speed, steering, braking, and suspension state. At high speed, where the wings and tunnels produce plenty, it **reduces fan suction to cap total downforce at ~21 kN**. That keeps peak cornering loads near ~5 G for the driver and within tyre load limits, and saves fan power on straights.

Estimated at race start (~960 kg, including active suspension and load-rated tyres; see [weight-budget.md](weight-budget.md)), with racing slicks at a ~1.6 grip coefficient:

| Speed | Fan (kN) | Tunnels + wings (kN) | Total (kN) | Peak cornering grip | F1 estimate (same method) |
| --- | --- | --- | --- | --- | --- |
| 100 km/h | 12 | ~2 | ~14 | **~4.0 G** | ~2.2 G |
| 150 km/h | 12 | ~5 | ~17 | **~4.5 G** | ~2.8 G |
| 250 km/h | ~6 | ~14 | ~20 | **~5.0 G** | ~5.0 G |
| 300 km/h | ~1 | ~20 | ~21 | **~5.2 G** | ~6.5 G (theoretical; real peaks ~6 G) |

The F1 column assumes ~17.5 kN at 250 km/h on a ~838 kg car (768 kg plus fuel), scaling with speed².

**Result:** Grip is nearly flat across the speed range. The car roughly **doubles F1's grip in slow corners**, matches it around 250 km/h, and gives up grip only in the fastest sweepers (above ~250 km/h), where the cap keeps the driver and tyres within limits. Raising the cap would recover that, at the cost of higher driver loads and tyre wear. This corrects the earlier ~4.7 G high-speed estimate, which assumed F1-level downforce with no fan.

### Aero Balance

- **Fan downforce acts near the middle of the floor** (~1.9 m behind the front axle), almost exactly at the CG (~1.9 m). Changing fan speed therefore barely shifts the balance, which keeps the car predictable as the controller blends sources.
- **Front wing flap** (automatic) trims balance: more front on corner entry for turn-in, less on exit to reduce understeer under power.

## Drag & Top Speed

The fan carries much of the low-speed downforce, so the wings are smaller than a pure wing car's:

| Configuration | Drag area (CdA) | Top speed at ~910 kW at the wheels |
| --- | --- | --- |
| Normal (DRS closed) | ~1.3 m² | **~375 km/h** |
| DRS open | ~1.1 m² | **~400 km/h** |

Both figures need full electric deployment at the end of the straight; on diesel power alone, top speed drops to ~315 km/h with DRS closed (see [powertrain.md](powertrain.md) M5).

## Active Aero (Automatic)

| Device | Controlled by | Purpose |
| --- | --- | --- |
| Fan speed | Speed, lateral and longitudinal g, suspension travel, coolant temperatures | Downforce schedule and cap; reduced on straights; low-speed radiator airflow |
| Radiator-to-fan duct valves | Speed, coolant temperatures | Open at low speed for fan-driven cooling, closed when ram air suffices |
| Front wing flap | Steering, braking, throttle | Balance trim through each corner phase |
| Sidepod cooling louvers | Coolant temperatures, speed ([cooling.md](cooling.md)) | Cooling at minimum drag |
| **Rear wing DRS flap** | **Driver (DRS button), Sporting Rule 16 conditions only** | Drag reduction for overtaking |

All automatic devices respond only to the car's operating state (Technical Rule 7). The DRS flap is the only driver-operated aero device, and the car's control system blocks it outside a valid zone or without the 1 s gap.

## Mass Changes

| Item | Mass (kg) |
| --- | --- |
| Lightweight underfloor fans, motors & inverters (2) | +5 |
| Fan duct and debris guards | +4 |
| Sliding skirts, springs & wear strips | +8 |
| Radiator-to-fan ducts and valves | +1 |
| Separate cooling fans deleted | −2 |
| Smaller front wing (12 → 10 kg) | −2 |
| Smaller rear wing assembly (13 → 11 kg) | −2 |
| **Net** | **+12** |

Car + driver rises from ~835 kg to **~847 kg** (later ~862 kg with active suspension and load-rated tyres), and fuel from ~90 kg to **~94 kg**. See [weight-budget.md](weight-budget.md). Active suspension ([suspension.md](suspension.md)) holds the floor height and attitude so the skirts and tunnels work consistently.

## Open Items

1. **Floor, tunnel, and diffuser shapes:** Needs CFD-level work; this document sizes the downforce targets only.
2. ~~Tyre loads~~ **Done:** load-rated W fronts and HD rears cover the ~30 kN peak ([tyres.md](tyres.md)).

## Decisions

- **Skirt wear strips:** Not safety parts. Fitted fresh before each race; a mid-race replacement uses one swap, shared with any tyre change in the same stop (Sporting Rule 2).
- **Debris guards:** Safety parts (Sporting Rule 5), freely replaceable.
- **Shared cooling:** The underfloor fans also pull radiator air at low speed, replacing the separate cooling fans.
- **Fan hardware:** Lightweight (~2.5 kg per fan unit), not heavy-duty.
