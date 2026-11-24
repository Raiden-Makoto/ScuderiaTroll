# Weight Budget

Component-level mass budget for the ScuderiaTroll car, using the powertrain in [powertrain.md](powertrain.md), the aftertreatment in [aftertreatment.md](aftertreatment.md), and the cooling system in [cooling.md](cooling.md).

All figures are design estimates for a fictional vehicle. Chassis items are benchmarked against a 2026-style F1 car; powertrain items are derived from the adopted specifications. Treat the total as roughly ±40 kg.

## Reference: FIA Minimum Weight

Technical Rule 6 keeps the standard FIA minimum weight, measured without fuel or DEF (urea). Using the 2026 F1 figure:

- **768 kg**, including the driver (80 kg allowance, including seat and any ballast needed to reach it).

Being over the minimum is legal; the minimum is only a floor.

## Assumptions

- 4 wheels (2-axle layout, wheelbase ≤ 3.6 m under Technical Rule 3).
- Carbon-composite monocoque, bodywork, wings, and wishbones at F1-equivalent technology. Carbon remains lighter and stiffer than any metal for these parts.
- **Alloy X** (~2.7 g/cm³, titanium-level strength; see [powertrain.md](powertrain.md)) replaces titanium, steel, and aluminium wherever a part must be metal.
- The Halo stays standard FIA titanium (7 kg): Technical Rule 6 keeps standard FIA safety structures, so it isn't swapped to Alloy X.
- Gear teeth and bearings stay steel, which is still needed for contact fatigue.

## Budget

### Chassis & Vehicle Systems

| Component | Mass (kg) | Notes |
| --- | --- | --- |
| Monocoque (survival cell) | 45 | FIA survival cell, carbon |
| Halo | 7 | Standard FIA titanium |
| Front, rear & side crash structures | 15 | |
| Floor, bodywork & sidepods | 55 | Includes active cooling louvers |
| Front wing | 10 | Smaller than F1's thanks to the underfloor fan; automatic balance flap |
| Rear wing & beam wing | 11 | Includes the DRS flap and actuator |
| Underfloor fans, motors & inverters (2) | 5 | Lightweight, 2 × 12.5 kW; also provide low-speed radiator cooling ([aero.md](aero.md)) |
| Fan duct & debris guards | 4 | Debris guards are safety parts (Sporting Rule 5) |
| Sliding skirts, springs & wear strips | 8 | |
| Suspension (all four corners) | 60 | Carbon wishbones and pushrods/pullrods; Alloy X uprights and rod ends; fully active electromechanical actuators with passive springs ([suspension.md](suspension.md)) |
| Wheels & tyres | 81 | W fronts (~20 kg each) and HD rears (~20.5 kg each) on forged magnesium rims ([tyres.md](tyres.md)) |
| Brakes | 29 | Carbon discs, Alloy X calipers, brake-by-wire, ducts; smaller rear brakes thanks to MGU-K regen |
| Steering | 10 | |
| Electronics, wiring loom & sensors | 30 | Includes emissions logging (Rule 4) |
| Engine & ancillary cooling | 41 | Radiators, oil coolers, pipework, fluids, radiator-to-fan ducts and valves ([cooling.md](cooling.md)) |
| Hydraulics | 12 | |
| Fire suppression | 5 | |
| Fuel cell & pumps | 12 | ~120 L bladder for 94 kg of HVO |
| Miscellaneous | 13 | Alloy X fasteners, mirrors, cameras, transponder, paint |
| **Subtotal** | **453** | |

### Powertrain

| Component | Mass (kg) | Notes |
| --- | --- | --- |
| OP4 engine, dry | 109 | 3.2 L; 3D-printed Alloy X block and crankcase with load-path-optimised walls; Alloy X crankshafts and geartrain; no heads or valvetrain |
| Gearbox, clutch & rear differential | 45 | 6-speed; Alloy X casing, steel gears; rated for ~860 Nm diesel torque plus rear MGU-K |
| Two-stage e-turbos (2 × MGU-H) | 21 | Alloy X turbine housings |
| Charge-air coolers & piping | 15 | Two water-cooled charge-air coolers on the LT loop |
| Exhaust manifold & piping | 5 | Single-sided, Alloy X |
| Aftertreatment, dry | 14 | DOC + SDPF + cleanup SCR, cans, DEF hardware (inter-stage layout) |
| Rear MGU-K (200 kW) | 18 | |
| Front MGU-Ks (2 × 125 kW), with integrated inverters | 28 | Inboard, one per front wheel |
| Rear inverter | 4 | |
| High-voltage cabling | 6 | Includes front runs |
| Front driveshafts | 6 | No front differential |
| Battery (450 kW, ~4.5 kWh) | 50 | ~45 kg cells and pack, plus mounting and cooling plates |
| Extra cooling for electric systems | 8 | Battery, motors, inverters |
| **Subtotal** | **329** | |

### Total

| Item | Mass (kg) |
| --- | --- |
| Chassis, aero & vehicle systems | 453 |
| Powertrain | 329 |
| Driver (FIA allowance) | 80 |
| **Car + driver (minimum-weight condition)** | **862** |
| Fuel (HVO) | 94 |
| DEF | 4 |
| **Race start** | **~960** |

**Result: ~862 kg, ~94 kg over the 768 kg FIA minimum.**

## Reductions Applied

Starting from a first-pass total of ~903 kg (before cooling fans were added):

### Round 1: Novel Alloys, Gearbox, Brakes

| Change | Saving (kg) |
| --- | --- |
| Novel-alloy engine block and crankcase | 18 |
| Novel-alloy crankshafts and geartrain | 6 |
| 6-speed gearbox instead of 8 (the diesel's wide band plus electric torque fill makes extra ratios unnecessary) | 6 |
| Novel-alloy turbo housings and exhaust manifold | 5 |
| Front motors with integrated inverters | 4 |
| Smaller rear brakes (rear MGU-K regen takes much of the rear braking load) | 4 |
| Novel-alloy suspension uprights | 3 |
| **Total** | **46** |

The cooling fans then added 2 kg, giving 859 kg.

### Round 2: Lighter Alloy X, Optimised Walls, Wider Alloy X Use

| Change | Saving (kg) |
| --- | --- |
| Alloy X density cut from 3.2 to 2.7 g/cm³ (engine block, crankcase, crankshafts, geartrain) | 9 |
| Load-path-optimised printed block walls | 3 |
| Alloy X gearbox casing | 4 |
| Lighter Alloy X turbo housings and exhaust manifold | 2 |
| Lighter Alloy X uprights, plus Alloy X rod ends | 2 |
| Alloy X brake calipers (replacing aluminium-lithium) | 2 |
| Alloy X fasteners (replacing titanium) | 2 |
| **Total** | **24** |

Giving 835 kg.

### Round 3: Fan-Assisted Ground Effect (Additions)

| Change | Mass (kg) |
| --- | --- |
| Lightweight underfloor fans, motors & inverters | +5 |
| Fan duct & debris guards | +4 |
| Sliding skirts | +8 |
| Radiator-to-fan ducts and valves | +1 |
| Separate cooling fans deleted (underfloor fans take over) | −2 |
| Smaller front and rear wings | −4 |
| **Net** | **+12** |

Giving 847 kg.

### Round 4: Active Suspension (Addition)

| Change | Mass (kg) |
| --- | --- |
| Fully active electromechanical suspension, net of deleted dampers, heave springs, and anti-roll bars | +10 |

Giving 857 kg. Holding the floor at a steady height and attitude keeps the fan and ground-effect downforce consistent ([suspension.md](suspension.md)).

### Round 5: Tyres Rated for the Loads

| Change | Mass (kg) |
| --- | --- |
| W (380 mm) fronts instead of F1-like 305 mm | +2 |
| HD (405 mm, reinforced) rears instead of F1-like 380 mm | +3 |
| **Net** | **+5** |

Giving 862 kg. The car's peak per-tyre loads (~13.4 kN rear, ~10.9 kN front) need these ratings ([tyres.md](tyres.md)).

The fans also draw ~15 kW on average, adding ~4 kg of fuel (90 → 94 kg). The trade buys roughly double F1's slow-corner grip ([aero.md](aero.md)).

Options considered and rejected:

- **Smaller battery:** Would cut electric power below 450 kW and break the 55/45 split.
- **Less fuel:** Fuel load is set by the race distance and diesel efficiency.
- **Dropping front drive:** Saves ~35 kg but loses AWD traction, torque vectoring, and most of the front regen.
- **Alloy X monocoque or bodywork:** Carbon composite is still lighter and stiffer for large panels and shells.
- **Alloy X Halo:** Would save ~3 kg but breaks the standard FIA safety structure requirement (Rule 6).
- **Alloy X wheel rims:** Forged magnesium (~1.8 g/cm³) is already lighter for rims.

## Where the Remaining Excess Comes From

The ~94 kg excess comes from the powertrain, the fan system, active suspension, and the heavier-rated tyres those loads require. The main contributors, compared with an F1 car:

- **Wider, heavier-rated tyres (~5 kg).**

- **Underfloor fan system and skirts (~12 kg net):** Deliberate, for slow-corner grip.
- **Active suspension (~10 kg net):** Deliberate, to keep the floor working.

- **Front motors, inverters, driveshafts (~40 kg):** F1 cars have no front drive.
- **Second turbo stage and charge-air cooler (~15 kg).**
- **Battery (~15 kg over F1):** 450 kW needs ~45 kg of high-power cells.
- **Aftertreatment (~14 kg):** F1 cars have none.

Partly offset by the Alloy X engine (now close to F1 V6 weight despite diesel-strength structure), smaller rear brakes, and Alloy X chassis parts.

## Performance Impact

| Metric | 2026 F1 (estimate) | ScuderiaTroll at 862 kg |
| --- | --- | --- |
| Power | ~1,000 hp | ~1,350 hp |
| Power-to-weight, race start | ~1.19 hp/kg (768 + 70 kg fuel) | ~1.41 hp/kg (862 + 98 kg fluids) |
| Power-to-weight, race end | ~1.30 hp/kg | ~1.57 hp/kg |

Power-to-weight is ~18–21% better than F1, so straight-line acceleration wins. The extra ~94 kg costs:

- **Braking & cornering:** Every corner needs more grip for the same speed. The underfloor fan more than covers this in slow and medium corners; in the fastest sweepers the car gives up some grip to F1 ([aero.md](aero.md)).
- **Tyre wear:** Heavier loads wear tyres faster, even with load-rated sizes; active suspension's tyre load management partly offsets this ([tyres.md](tyres.md)). With only 3 swaps per race (Sporting Rule 2), tyre management becomes a central strategy problem.
- **Front-axle regen helps here:** More mass means more braking energy to recover, so the larger battery and front motors partly pay for themselves.

## Open Items

1. ~~Weight distribution~~ **Done:** [layout.md](layout.md) puts the split at ~45/55 front/rear with a ~0.31 m CG height, inside the F1 window without ballast.
2. ~~Tyre specification~~ **Done:** single control supplier with a catalogue of load-rated sizes (Sporting Rule 17); W fronts and HD rears ([tyres.md](tyres.md)).
