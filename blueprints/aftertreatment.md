# Aftertreatment Sizing

First-pass sizing of the exhaust aftertreatment for the OP4 diesel-electric powertrain (see [powertrain.md](powertrain.md)), targeting Technical Rule 4: race-averaged emissions below EPA Tier 4 line-haul locomotive limits.

ScuderiaTroll is a fictional vehicle, so there is no test data: the assumptions below are adopted as the design values, chosen to be physically plausible. Exhaust flow scales with diesel power, not displacement, so if the diesel is de-rated (see powertrain review M1), scale volumes and DEF use roughly linearly with peak power.

## Assumptions

| Parameter | Value | Basis |
| --- | --- | --- |
| Peak diesel power | 560 kW (750 hp) | Powertrain concept |
| Race diesel energy | ~548 kWh (~735 bhp-hr) | ~1.5 h race, diesel averaging ~65% of peak |
| Brake specific fuel consumption | ~164 g/kWh | 50% thermal efficiency, HVO at ~44 MJ/kg |
| Peak fuel flow | ~25.5 g/s | |
| Trapped air-fuel ratio | λ ≈ 1.4 (HVO stoichiometric ≈ 15:1) | Typical full-load racing diesel |
| Scavenging delivery ratio | ~1.2 | Opposed-piston two-stroke; extra air passes straight through to the exhaust |
| Peak exhaust mass flow | ~0.7 kg/s ≈ 1,950 Nm³/h | |
| Fuel sulphur | ~0 ppm | HVO is sulphur-free, which protects the catalysts |

## Emissions Budget

Tier 4 limits are in g/bhp-hr (1 g/bhp-hr = 1.341 g/kWh). Each design target is 70% of its limit, leaving margin for Safety Car periods, cold starts, and catalyst ageing.

| Pollutant | Limit (g/bhp-hr) | Limit (g/kWh) | Allowed per race | Design target (g/kWh) |
| --- | --- | --- | --- | --- |
| NOx | 1.3 | 1.74 | ~955 g | 1.22 |
| PM | 0.03 | 0.040 | ~22 g | 0.028 |
| HC | 0.14 | 0.188 | ~103 g | 0.13 |
| CO | 1.5 | 2.01 | ~1,100 g | 1.41 |

### Required Conversion Efficiency

Assumed engine-out emissions for a high-output diesel on HVO, with moderate injection retard and internal EGR (residual gas trapping via scavenging control):

| Pollutant | Engine-out (g/kWh) | Required reduction | Typical capability |
| --- | --- | --- | --- |
| NOx | ~6.0 | ~80% | SCR: 80–95% when warm |
| PM | ~0.15 | ~81% | Wall-flow DPF: 95%+ |
| HC | ~0.5 | ~74% | DOC: 90%+ above ~250 °C |
| CO | ~3.0 | ~53% | DOC: 90%+ above ~250 °C |

NOx is the sizing case: it needs the most reduction, and SCR is the component closest to its limit. PM, HC, and CO have large margins.

## Recommended Layout

```
Engine → HP turbine (MGU-H) → DOC → DEF injector + mixer → SDPF → cleanup SCR + ASC → LP turbine → tailpipe
```

**Components:**

- **DOC (diesel oxidation catalyst):** Pt/Pd on metallic foil substrate. Burns HC and CO, and converts NO to NO2, which speeds up both SCR and soot burn-off.
- **SDPF (SCR-coated diesel particulate filter):** A wall-flow silicon carbide filter with SCR catalyst coated in its walls. This combines particulate filtering and most of the NOx reduction in one brick, saving a large amount of volume over a separate DPF + SCR.
- **Cleanup SCR + ASC:** A small SCR brick to finish the NOx reduction, with an ammonia slip catalyst (ASC) zone on its rear face to stop unreacted ammonia escaping. Ammonia isn't a Rule 4 pollutant, but it is harmful and the coating is cheap insurance.
- **DEF (diesel exhaust fluid) system:** Injector and compact swirl mixer upstream of the SDPF. Urea needs some distance and heat to convert into ammonia; the hot inter-stage location helps.

### Placement: Between Turbine Stages

This layout uses the adopted series (compound) two-stage turbocharging. The aftertreatment sits between the high-pressure and low-pressure turbines, rather than after both as on a road car. Large marine diesels use the same principle (pre-turbine SCR).

Advantages:

- **Smaller bricks:** At ~2.0–2.5 bar and ~500–600 °C, the gas occupies ~40% less volume than after the last turbine (~1.1 bar, ~400 °C). For the same residence time, the bricks shrink by ~35–40%.
- **Stays hot:** The catalysts stay above light-off far longer under Safety Car and in the pit lane, which helps the race average.
- **Self-cleaning filter:** Above ~550 °C, soot burns off with oxygen continuously. At lower temperatures, soot burn-off relies on NO2, which the SCR coating in an SDPF competes for.
- **Lower backpressure cost:** Lower volumetric flow means less pumping loss for the same pressure drop, and the LP turbine and MGU-H still recover energy downstream.

Costs:

- **Thermal lag on the LP turbine:** The bricks act as a heat sink between the turbine stages. The MGU-H covers this by motoring the turbo.
- **Pressure-rated canning:** Housings must hold ~2.5 bar at up to ~650 °C (during filter regeneration).
- **Catalyst choice:** Copper-zeolite SCR loses efficiency above ~450–500 °C, as ammonia starts oxidising instead of reacting with NOx. Use **iron-zeolite** (effective ~350–600 °C), or a mixed Cu/Fe formulation.

The post-turbine sizes below are kept for comparison only.

## Component Sizes

Sized on peak exhaust flow (~1,950 Nm³/h). GHSV (gas hourly space velocity) is the standard catalyst sizing measure: standard-condition gas flow per hour divided by brick volume. Road and truck systems typically run 30,000–150,000 h⁻¹. These sizes run higher, which is acceptable because the catalysts operate hot and compliance is race-averaged.

| Component | Substrate | GHSV at peak (h⁻¹) | Post-turbine volume | Inter-stage volume |
| --- | --- | --- | --- | --- |
| DOC | Metallic foil, 600 cpsi | ~300,000 | ~6.5 L | ~4 L |
| SDPF | SiC wall-flow, SCR-coated (Fe-zeolite) | ~150,000 | ~13 L | ~8 L |
| Cleanup SCR + ASC | Cordierite or metallic, 600 cpsi | ~400,000 | ~5 L | ~3 L |
| **Total brick volume** | | | **~24.5 L** | **~15 L** |

### Mass Estimate

| Item | Post-turbine | Inter-stage |
| --- | --- | --- |
| Bricks | ~10–12 kg | ~6–8 kg |
| Cans, insulation, mixer, mounts | ~5 kg | ~4–5 kg (pressure-rated) |
| DEF system, dry (tank, pump, injector, lines) | ~3 kg | ~3 kg |
| DEF fluid (race fill) | ~3–5 kg | ~3–5 kg |
| **Total (wet, race start)** | **~21–25 kg** | **~16–21 kg** |

DEF fluid burns off during the race, so the system is ~3–5 kg lighter at the flag.

### Backpressure

Allow ~15 kPa pressure drop across the full system at peak flow:

- **Post-turbine:** ~15 kPa × ~1.2 m³/s ≈ **18 kW** pumping loss (~3% of diesel peak).
- **Inter-stage:** ~15 kPa × ~0.75 m³/s ≈ **11 kW** (~2%).

Two-stroke engines are especially sensitive to backpressure, because scavenging depends on intake pressure staying above exhaust pressure. The e-turbo boost must account for this.

## Consumables & Maintenance

### DEF Consumption

Reducing NOx from ~6.0 to ~1.2 g/kWh over ~548 kWh removes ~2.6 kg of NOx. At a 1:1 ammonia-to-NOx molar ratio, that needs ~1.7 kg of urea, or **~5.3 kg (~4.8 L) of DEF** (32.5% urea solution). If engine-out NOx can be brought down to ~4 g/kWh, DEF use drops to ~3.1 kg.

Specify a **~6 L DEF tank** for margin. Freezing isn't a concern at race temperatures, so heated lines aren't needed.

### Soot & Ash

- **Soot:** ~0.15 g/kWh × 548 kWh ≈ **82 g per race** engine-out. At 95%+ filtration, ~4 g leaves the tailpipe, well under the ~22 g race allowance. At inter-stage temperatures, soot burns off continuously, so the filter never needs a dedicated regeneration cycle mid-race.
- **Ash:** Non-combustible lube-oil residue builds up in the filter and must be cleaned out between events. Two-stroke opposed-piston engines have no crankcase scavenging, so oil consumption (and ash) should be modest. Aftertreatment parts are classified as safety parts (Sporting Rule 5), so filters can be swapped for cleaning as often as needed without penalty.

## Compliance Monitoring

Rule 4 compliance is race-averaged, so the car must log emissions through the whole race:

- **NOx:** Sensors before the DEF injector (for dosing control) and after the cleanup SCR (for compliance).
- **PM:** A soot sensor after the SDPF.
- **HC & CO:** No practical real-time sensors at this size; use calibrated DOC efficiency maps plus exhaust temperature.
- **Exhaust flow & diesel energy:** From the engine ECU (fuel flow, air flow, crank power), to convert concentrations into g/bhp-hr.

## Decisions

- **Turbo layout:** Series (compound) two-stage turbocharging is adopted, so the inter-stage placement and sizes above apply.
- **Engine-out NOx:** ~6 g/kWh is the adopted design value (no test data for a fictional vehicle).
- **Blown diffuser:** Dropped. The exhaust exits through a plain tailpipe after the LP turbine.
- **Classification:** Aftertreatment is a safety part, not a power unit part (Sporting Rule 5), and can be replaced without limit or penalty.
