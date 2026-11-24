# Cooling Strategy

Cooling design for the ScuderiaTroll powertrain (see [powertrain.md](powertrain.md)). Replaces the original "open louvers under braking, close on straights" idea, which had the logic backwards: heat generation peaks at full throttle on straights, not in slow corners.

All figures are design estimates for a fictional vehicle.

## Heat Loads

At peak (full throttle, full electric deployment) and averaged over a lap (diesel averaging ~65% of peak):

| Source | Peak (kW) | Lap average (kW) | Notes |
| --- | --- | --- | --- |
| Engine coolant & oil | ~200 | ~130 | ~18% of the ~1,120 kW fuel energy at 560 kW and 50% efficiency |
| Charge air (two intercoolers) | ~120 | ~70 | ~0.64 kg/s compressed to ~4.5 bar absolute, cooled from ~200 °C back to ~50 °C |
| Electric systems | ~45 | ~20 | Motors (~95% efficient), inverters (~98%), battery losses at 450 kW |
| **Total to air** | **~365** | **~220** | |

The remaining engine heat leaves through the exhaust (partly recovered by the MGU-H turbines) and doesn't need radiators.

## Strategy

### 1. Three Cooling Loops

| Loop | Temperature | Serves | Radiator location |
| --- | --- | --- | --- |
| High-temperature (HT) | ~110–120 °C, pressurised to ~3.5 bar | Engine coolant, engine oil | Sidepods |
| Low-temperature (LT) | ~60–65 °C | Water-cooled charge-air coolers (both stages), motors, inverters | Sidepods, **ahead of** the HT cores so they get the coolest air |
| Battery | ~45–55 °C | Battery pack (dielectric fluid); cells rated to 60 °C | Small dedicated core in the airbox |

- **Pressurised HT loop:** Running coolant hotter increases the temperature gap to ambient air, so each kW needs less radiator area and less airflow, which means less drag.
- **Water-cooled charge-air coolers:** Instead of large air-to-air intercoolers in the airstream, both compressor stages dump heat into the LT loop. The coolers can sit right next to the compressors, shortening charge-air piping, and the LT radiators can go wherever packaging suits.
- **Separate battery loop:** Lithium cells need to stay much cooler than the motors and inverters, so the battery gets its own small loop. Using cells rated to 60 °C lets the loop run at ~45–55 °C, so it can still reject heat to 40 °C air without a refrigeration chiller.

### 2. Louvers Controlled by Temperature, Not Track Position

Sidepod louvers and inlet flaps are driven by a controller that holds the coolant temperatures, not by braking zones:

- **At high speed:** Ram airflow per unit of inlet area is high, so the controller *partly closes* the louvers while still passing enough air to reject full-throttle heat. This keeps the drag benefit the original idea wanted, but for the right reason.
- **At low speed:** Airflow per unit of area is low, so louvers open fully to keep enough mass flow through the cores. Drag at low speed is small, so this costs little lap time.
- **Never fully shut under load:** The original "snap shut on straights" would stop cooling exactly when heat output peaks.

This complies with Technical Rule 4's power-delivery clause: cooling controls aren't power-delivery modes and respond only to the car's thermal state.

### 3. Predictive Pre-Cooling

The controller uses a track map to manage the cooling system's stored heat:

- **Thermal buffer:** The engine block, oil, and coolant together hold ~100 kJ per °C. Letting the HT loop swing 10 °C stores ~1 MJ, roughly 10 s of a 100 kW deficit between heat produced and heat rejected.
- **Before a long straight:** Open the louvers early to pull coolant down to the bottom of its range.
- **On the straight:** Close down toward minimum drag and let the temperature climb, using the buffer.
- **Limit:** The buffer covers ~10 s, which isn't enough for a kilometre-long straight (~12–15 s at 300+ km/h). On those circuits, louvers stay partly open on the straight.

### 4. Underfloor Fans for Low-Speed Cooling

There are no separate cooling fans. Ducts run from the sidepod radiator exits to the underfloor fan plenum ([aero.md](aero.md)), and the underfloor fans pull air through the radiators when ram airflow isn't enough:

- **Safety Car and pit lane:** The engine still makes heat, but the car moves too slowly for ram cooling.
- **Grid and garage:** No ram airflow at all.
- **Control:** A valve in each duct opens at low speed and closes when ram air suffices. Pulling ~1.5 m³/s through the radiators to reject ~70 kW adds ~9 kW of fan power, within the fans' 25 kW rating.

### 5. Hot-Race Sizing

Radiators are sized for ~40 °C ambient (e.g. Bahrain, Qatar). At those races, louvers run more open and the car carries more cooling drag; at cool races, louvers close further and the car gains top speed.

## Radiator & Inlet Sizing

### Design Point

- **Hot race:** 40 °C ambient (air density ~1.13 kg/m³).
- **Speed:** Sustained full throttle at 200 km/h, with ~25% of car speed reaching the core face (~14 m/s) through a diffusing inlet duct.
- **Heat loads at peak:** HT ~200 kW, LT ~155 kW (charge air ~120 kW plus motors and inverters ~35 kW), battery ~10 kW peak / ~5 kW average.

### Stacked Cores: LT First, HT Behind

The LT loop runs cold relative to the air (only ~25 °C above a 40 °C ambient), so it's the hard one to cool and gets the coolest air. Air passes through the LT core first, warms to ~58 °C, then passes through the HT core, which at ~115 °C still has a ~57 °C margin over that air.

| Core | Heat (kW) | Coolant vs. incoming air | Effectiveness needed | Air mass flow |
| --- | --- | --- | --- | --- |
| LT (front of stack) | ~155 | ~65 °C vs. 40 °C (25 °C margin) | ~0.75 (deep core) | **~8.2 kg/s** |
| HT (rear of stack) | ~200 | ~115 °C vs. ~58 °C (57 °C margin) | ~0.43 (easy) | Same ~8.2 kg/s |

The LT core sets the airflow; the HT core just uses the same air.

### Core and Inlet Areas

| Item | Total (both sides) | Per sidepod |
| --- | --- | --- |
| Radiator core face area (LT + HT stacked) | ~0.52 m² | ~0.26 m² (e.g. ~0.58 × 0.45 m, steeply inclined in the sidepod) |
| Sidepod inlet area (fully open) | ~0.26 m² | ~0.13 m² (e.g. ~0.45 × 0.29 m) |
| Battery core (airbox) | ~0.05 m² | — |

- **Inlets** are sized at a ~0.5 inlet-to-car velocity ratio at 200 km/h. At higher speeds the louvers partly close, because the same mass flow needs less area.
- **Battery core:** Sized for the ~5 kW average heat load; the 45 kg pack's thermal mass (~45 kJ per °C) absorbs 10 kW peaks with only a few degrees of rise.
- **Cooler days:** At 25 °C ambient, the LT margin rises from 25 °C to 40 °C, so the louvers run much more closed and cooling drag falls accordingly.

### Cooling Drag

Air passing through the cores loses momentum, which shows up as drag. At 300 km/h with ~8.2 kg/s through the cores and ~60% of the momentum lost, cooling drag is **~410 N (~34 kW)**, equivalent to a drag area of ~0.1 m². That's included in the ~1.3 m² total drag area in [aero.md](aero.md). On cooler days it's lower.

### Low Speed

Below ~100 km/h, ram air can't supply ~8 kg/s; the underfloor fans pull ~1.5 m³/s through the radiators instead (section 4), enough for the ~70 kW rejected at Safety Car pace.

## Mass

| Item | Mass (kg) | Budget line in [weight-budget.md](weight-budget.md) |
| --- | --- | --- |
| HT radiators, pipework, coolant, oil coolers | ~40 | Engine & ancillary cooling |
| Radiator-to-fan ducts and valves | ~1 | Engine & ancillary cooling (now 41 kg) |
| Water-cooled charge-air coolers & LT piping | ~15 | Intercoolers & charge-air piping |
| LT radiator share & battery loop | ~8 | Extra cooling for electric systems |
| **Total** | **~64** | |

## Open Items

1. ~~Radiator core area and inlet sizing~~ **Done:** see "Radiator & Inlet Sizing" above (~0.52 m² of stacked cores, ~0.26 m² of inlets).
2. ~~Fan-assisted downforce~~ **Done:** the underfloor fans in [aero.md](aero.md) now handle low-speed cooling too.
