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
| Low-temperature (LT) | ~50–60 °C | Water-cooled charge-air coolers (both stages), motors, inverters | Sidepods, behind HT cores |
| Battery | ~30–45 °C | Battery pack (dielectric fluid) | Small dedicated core in the engine cover intake |

- **Pressurised HT loop:** Running coolant hotter increases the temperature gap to ambient air, so each kW needs less radiator area and less airflow, which means less drag.
- **Water-cooled charge-air coolers:** Instead of large air-to-air intercoolers in the airstream, both compressor stages dump heat into the LT loop. The coolers can sit right next to the compressors, shortening charge-air piping, and the LT radiators can go wherever packaging suits.
- **Separate battery loop:** Lithium cells need to stay much cooler than the motors and inverters, so the battery gets its own small loop.

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

### 4. Electric Fans for Low Speed

Two ~2 kW electric fans pull air through the sidepod cores when ram airflow isn't enough:

- **Safety Car and pit lane:** The engine still makes heat, but the car moves too slowly for ram cooling.
- **Grid and garage:** No ram airflow at all.

The fans are for cooling only, and are sized well below anything that would generate meaningful downforce. Fan cars are legal under Technical Rule 7, but a dual-purpose fan would need its own design study.

### 5. Hot-Race Sizing

Radiators are sized for ~40 °C ambient (e.g. Bahrain, Qatar). At those races, louvers run more open and the car carries more cooling drag; at cool races, louvers close further and the car gains top speed.

## Mass

| Item | Mass (kg) | Budget line in [weight-budget.md](weight-budget.md) |
| --- | --- | --- |
| HT radiators, pipework, coolant, oil coolers | ~40 | Engine & ancillary cooling |
| Electric fans (2) and controller | ~2 | Engine & ancillary cooling (now 42 kg) |
| Water-cooled charge-air coolers & LT piping | ~15 | Intercoolers & charge-air piping |
| LT radiator share & battery loop | ~8 | Extra cooling for electric systems |
| **Total** | **~65** | |

## Open Items

1. **Radiator core area and inlet sizing:** Needs the layout drawing (sidepod volume and inlet positions).
2. **Fan-assisted downforce:** Whether to exploit Rule 7 with a dual-purpose fan is a separate design decision.
