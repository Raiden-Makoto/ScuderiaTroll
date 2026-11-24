# Powertrain Design

## Concept

A clean diesel-electric **parallel hybrid** (inspired by BAE HybriDrive) with a **55% diesel / 45% electric** power split. The diesel drives the rear wheels through the gearbox, assisted by a rear MGU-K, while one MGU-K per front wheel provides electric all-wheel drive with torque vectoring. It runs on 100% HVO (Hydrotreated Vegetable Oil) renewable diesel, with an oxidation catalyst + SCR-coated particulate filter + Selective Catalytic Reduction (SCR) aftertreatment system (see [aftertreatment.md](aftertreatment.md)).

This targets Technical Rule 4: race-averaged exhaust below EPA Tier 4 locomotive limits, with HVO as the alternative fuel that keeps the car from being purely electric.

### Key Specifications

| Item | Value |
| --- | --- |
| Engine | OP4: opposed-piston two-stroke diesel, 4 cylinders / 8 pistons, two crankshafts |
| Displacement | 3.2 L (bore 86 mm, stroke 2 × 69 mm) |
| Diesel output | 560 kW (750 hp) at 6,200 RPM, ~860 Nm |
| BMEP | ~17 bar (≈34 bar four-stroke equivalent) |
| Boost | ~3–3.5 bar gauge (~4–4.5 bar absolute), two-stage series e-turbos |
| Electric output | 450 kW (two front MGU-Ks at 125 kW each, rear MGU-K 200 kW) |
| Total output | ~1,010 kW (~1,350 hp), 55% diesel / 45% electric |
| Battery | ~45 kg high-power lithium, ~4.5 kWh total, ~8 MJ usable |
| Fuel | ~94 kg HVO per race (includes ~4 kg for the underfloor fans) |
| Aftertreatment | ~16–21 kg wet ([aftertreatment.md](aftertreatment.md)) |

### Core Features

- **Variable-geometry compound (series) turbocharging:** Two electric-assisted turbos (MGU-H) in series. A single exhaust manifold on the engine's exhaust-port side feeds a high-pressure turbo, the aftertreatment sits between stages, and a low-pressure turbo harvests the remaining energy. The intake side runs low-pressure compressor → intercooler → high-pressure compressor → intercooler. The MGU-H motors eliminate turbo lag and provide scavenging air at low engine speeds.
- **No fuel-flow limit = massive boost:** Real F1 caps fuel flow to control power. Without that cap, the two-stage turbos run ~3–3.5 bar gauge (~45–50 psi) of boost, turning a 3.2 L opposed-piston block into a 750 hp (560 kW) engine on its own.
- **Front-axle regen, AWD & torque vectoring:** Two 125 kW front MGU-Ks, one per front wheel, alongside a 200 kW rear MGU-K. The front motors are mounted inboard (keeping unsprung mass low) and drive each wheel through a short driveshaft, with no front differential. Controlling each front wheel independently allows torque vectoring: more drive to the outside wheel helps rotate the car on corner entry and exit. Costs ~5–10 kg over a single front motor, partly offset by deleting the front differential. Out of slow corners the car is traction-limited, not power-limited, so driving all four wheels puts far more of the ~1,350 hp down than rear-wheel drive could, and spreads the work across four tyres instead of two.
- **Active, temperature-controlled cooling:** Three cooling loops (high-temperature engine, low-temperature charge-air/electric, battery) with sidepod louvers driven by coolant temperature and speed: partly closed at high speed where ram air is plentiful, fully open at low speed, with predictive pre-cooling before long straights, and the underfloor fans pulling air through the radiators for Safety Car and pit lane. See [cooling.md](cooling.md).

## Making It Fast

### 1. Keep It Lightweight (~862 kg)

See [weight-budget.md](weight-budget.md) for the component-level budget: ~862 kg (car + driver, no fuel or DEF), including the underfloor fan system, active suspension, and load-rated tyres, against the 768 kg FIA minimum.

Diesels run high peak cylinder pressures (200+ bar), but modern F1 engines already run in a similar range, so the structural penalty is smaller than diesel's reputation suggests. Alloy X's strength at temperature covers it without thick walls. To keep the car agile:

- **Alloy X stressed-member block (Rule 5):** A 3D-printed, finish-machined block and crankcase in Alloy X (see below) with steel cylinder liners, so the engine carries rear suspension loads directly without a heavy subframe.
- **High-power battery (~45 kg):** High-power lithium cells at ~10 kW/kg deliver the full 450 kW. The pack holds ~4.5 kWh, with ~8 MJ usable (enough for ~18 s of full deployment from full charge). Braking regen through both MGU-Ks plus MGU-H harvest on straights recovers ~7–8 MJ per lap, so the car can deploy full electric power for ~15–18 s every lap.
- **Fuel load (~94 kg):** At ~50% thermal efficiency, the diesel needs ~90 kg of HVO for a full race, plus ~4 kg to power the underfloor fans ([aero.md](aero.md)). Refuelling is only allowed in Overtime Shootouts (Sporting Rule 1), so the car starts with the full load.

#### Engine Block: Alloy X

Alloy X is the team's novel high-temperature light alloy, permitted under Technical Rule 5 because it can be produced and processed with standard factory equipment (metal 3D printers, CNC machines). Its design targets:

| Property | Alloy X target | Aluminium (A356-T6) | Titanium (Ti-6Al-4V) |
| --- | --- | --- | --- |
| Density | ~2.7 g/cm³ | 2.7 g/cm³ | 4.4 g/cm³ |
| Yield strength, room temperature | ≥ 900 MPa | ~200 MPa | ~880 MPa |
| Strength retained at 300 °C | ≥ 70% | ~30% | ~65% |
| Thermal conductivity | ≥ 60 W/m·K | ~150 W/m·K | ~7 W/m·K |
| Thermal expansion | ~12 × 10⁻⁶/K | ~21 × 10⁻⁶/K | ~9 × 10⁻⁶/K |

- **Aluminium's density with titanium's strength** is what makes Alloy X worth using across the car: it replaces titanium, steel, and aluminium in metal parts (engine, gearbox casing, turbo housings, uprights, brake calipers, fasteners). Carbon composite stays for the monocoque, bodywork, and wings, and the Halo stays standard FIA titanium.
- **Strength at temperature** lets the block carry diesel combustion loads and rear suspension loads without thick walls.
- **Thermal conductivity** is far better than titanium's, so heat moves out of the block into the coolant instead of building up around the liners.
- **Thermal expansion matched to steel** (~12 × 10⁻⁶/K) keeps the steel liners tight in the block across the full temperature range. This matters more than usual in an opposed-piston engine, because the intake and exhaust ports are cut into the liners themselves.

**Manufacturing process:** Large-format metal 3D printing (laser powder-bed fusion) to a near-net block, then CNC finish machining of the crank tunnels, liner bores, and mounting faces. Large-format printers count as standard factory equipment under Rule 5. Printing allows what casting can't:

- **Conformal coolant passages** that wrap tightly around each cylinder's exhaust-port band, the hottest part of an opposed-piston engine, instead of the simpler jackets casting cores can form.
- **Integrated scavenge-air plenum and coolant crossovers** printed into the block, deleting separate parts and joints.
- **Lattice-filled, load-path-optimised walls** where the block carries rear suspension loads as a stressed member.

### 2. Geared for 370+ km/h (230+ mph)

A 6,200 RPM redline doesn't make a car slow: gearing converts engine speed into road speed, so what matters is power at the wheels.

- **Tall overall gearing:** With 0.72 m tyres, 375 km/h is ~2,760 wheel RPM, so top gear needs an overall ratio of ~2.24:1 at 6,200 RPM, about half an F1 car's (~4.6:1 at ~12,000 RPM). The engine turns slower, but at equal power the wheel force is the same.
- **6-speed spacing:** First gear (~8.4:1 overall) tops out around 100 km/h. Six ratios from 8.4:1 to 2.24:1 give ~30% steps, so each upshift drops the engine from 6,200 to ~4,800 RPM, inside its 3,000–6,200 RPM working band. The electric motors fill the torque gap during each shift.
- **Front motors:** Fixed single-speed reduction of ~7:1 (motor ~20,000 RPM at top speed), no gearbox.
- **0–100 km/h (0–62 mph): ~2.0–2.1 s.** Traction-limited, not power-limited: with AWD, racing slicks (~1.6 grip coefficient without downforce), and ~960 kg at race start, the car can accelerate at ~1.6 g, which needs only ~400 kW at 100 km/h. The underfloor fan adds downforce from a standstill, so launch grip may be higher still; ~2.0 s is a conservative figure.
- **0–200 km/h: ~3.8 s.** Still mostly traction-limited, with fan and aero downforce adding grip as speed rises.
- **0–300 km/h (0–186 mph): ~7.5–8 s.** Power-limited above ~200 km/h, with drag taking a growing share. Uses ~3.4 MJ of battery energy, well within the ~8 MJ usable.
- **Top speed: ~375 km/h (233 mph) normally, ~400 km/h with DRS open,** at drag areas (CdA) of ~1.3 m² and ~1.1 m² with ~910 kW at the wheels ([aero.md](aero.md)). Both require full electric deployment at the end of the straight; on diesel power alone, top speed is ~315 km/h with DRS closed (see M5).

### 3. Fan-Assisted Ground Effect

See [aero.md](aero.md). Two electric underfloor fans suck air from beneath a skirt-sealed floor, adding ~12 kN of downforce at any speed, on top of ground-effect tunnels and smaller-than-F1 wings.

- **Slow-corner grip:** ~4.0 G at 100 km/h versus ~2.2 G for an F1 car.
- **Low engine cover:** The opposed-piston engine has no cylinder heads, so clean air flows straight over the cover onto the rear wing.
- **Active aero:** Fully automatic, except the DRS flap (Technical Rule 7, Sporting Rule 16).

## Comparison With a Real F1 Car

All figures are rough estimates: F1 values are commonly cited approximations, and ScuderiaTroll values are calculated from this document's specifications.

| Metric | 2026 F1 car (est.) | ScuderiaTroll OP4 diesel-electric (est.) |
| --- | --- | --- |
| Total power | ~1,000 hp (V6 hybrid) | ~1,350 hp (750 hp OP4 + 450 kW electric) |
| Mass (car + driver, no fuel) | 768 kg | ~862 kg |
| Drive layout | Rear-wheel drive | All-wheel drive (independent front motors with torque vectoring) |
| 0–200 km/h | ~4.4 s | ~3.8 s (AWD traction) |
| Top speed | ~355 km/h (220 mph) | ~375 km/h (~400 km/h with DRS), with electric deployment |
| Cornering grip at 100 km/h | ~2.2 G | ~4.0 G (underfloor fan) |
| Cornering grip at 250 km/h | ~5.0 G | ~5.0 G |

**Cornering grip:** Grip comes from tyre friction times (weight + downforce). Without a fan, the heavier car would have slightly less grip than F1 everywhere. The underfloor fan adds ~12 kN at any speed, so the car roughly doubles F1's grip in slow corners and matches it around 250 km/h. Above that, the active aero caps total downforce at ~21 kN for driver and tyre loads, so the car gives up some grip to F1 in the fastest sweepers. Full schedule in [aero.md](aero.md).

## How to Win

> "Horsepower sells cars, torque wins races." — Carroll Shelby

The quote is the team's spirit, but the real advantages are traction and power, not engine torque:

- **Corner exit domination:** Out of slow corners every car is traction-limited. AWD puts power through four tyres instead of two, and torque vectoring on the front axle helps the car rotate and straighten up earlier. The e-turbos hold full boost from the apex, so there's no lag before the diesel delivers.
- **Wide power band:** The engine works from 3,000 to 6,200 RPM with electric torque filling every shift, so the car needs only 6 gears and the driver can short-shift in the wet or to save tyres with little lap-time cost.
- **Straight-line speed:** ~1,350 hp against F1's ~1,000 hp, with ~20–25% better power-to-weight, wins the drag race out of every corner. On long straights, top speed depends on saving battery charge for the end of the straight (see M5).
- **Tyre management:** The heavier car wears tyres faster (see [weight-budget.md](weight-budget.md)), but AWD spreads traction and braking work across all four tyres, which partly offsets it. With only 3 swaps per race, this is where races are won or lost.

---

## Design Review

Severity levels:

- **Blocker:** Likely illegal under the Technical Regulations as written.
- **Major:** Physically implausible or self-contradictory; numbers need rework.
- **Minor:** Wording, terminology, or weak reasoning.

### Blockers

**B1. Emissions (Rule 4): resolved by rule change, now an engineering task.**
Rule 4 now defines "harmless" as below the EPA Tier 4 line-haul locomotive limits (NOx 1.3, PM 0.03, HC 0.14, CO 1.5 g/bhp-hr), with CO2 excluded. Production Tier 4 locomotive diesels meet these limits, so a diesel is legal in principle. First-pass sizing is in [aftertreatment.md](aftertreatment.md). What this design still needs:

- **A diesel oxidation catalyst (DOC):** The sketch lists SCR + DPF only. A DOC upstream is the standard way to clear HC and CO, and it also helps the DPF regenerate.
- **SCR sized for race output:** NOx 1.3 g/bhp-hr is ~1.7 g/kWh. With a ~90%-efficient SCR, engine-out NOx must stay below ~17 g/kWh, which a high-BMEP diesel can exceed. Combustion tuning (e.g. EGR, injection timing) and SCR sizing go together.
- **Exhaust temperature management:** SCR stops working below roughly 200 °C. Under Safety Car, in the pit lane, or after heavy MGU-H extraction, the exhaust can drop below that. Electric catalyst heating, or limiting MGU-H harvest when the catalyst is cold, may be needed.
- **DEF (urea) consumption:** Typically ~3–5% of fuel burned, so ~3–5 kg of DEF per race, plus tank and dosing hardware.
- **Race-averaged compliance:** Rule 4 measures emissions averaged over the whole race. Short spikes (e.g. cold-catalyst periods behind the Safety Car) are acceptable as long as clean running elsewhere brings the race average under the limits. That still requires on-board emissions logging to prove compliance.

**B2. Series-hybrid mode: resolved by rule change.**
The 60% electric cap has been replaced: Rule 4 now only bans purely battery-electric cars and requires an alternative fuel that genuinely contributes to propulsion. A series hybrid (diesel driving a generator, electric motors driving the wheels) is now legal, as is parallel or mixed operation. HVO counts as an alternative fuel (non-fossil). One engineering note remains: BAE HybriDrive is a transit-bus system, so little of its hardware carries over; treat it as inspiration, not a starting point.

**B3. Electric launch: resolved by rule change.**
With no electric cap, the AWD electric launch is legal. The ~2.1 s 0–100 km/h figure is now limited only by tyre grip and energy-store power (see M5).

**B4. MGU-H motoring: resolved by rule change.**
With no electric share to track, the MGU-H can motor the turbos freely for lag elimination and scavenging.

### Major

**M1. Displacement vs. power: resolved.**
750 hp at 6,200 RPM is ~860 Nm. At the original 2.2 L, that was a brake mean effective pressure (BMEP) of ~25 bar in a two-stroke, equivalent to ~49 bar in a four-stroke, beyond the 2014–2025 F1 V6 (roughly 39 bar equivalent). **Adopted:** displacement grows to 3.2 L, giving ~17 bar BMEP (≈34 bar four-stroke equivalent), below F1 V6 stress levels.

**6,200 RPM redline: resolved with mitigations.** Racing diesels have typically topped out around 5,000 RPM because diesel combustion takes a roughly fixed time (~2 ms), which at high RPM stretches across more crank angle and wastes energy into the exhaust. A two-stroke at 6,200 RPM also fires each cylinder ~103 times per second, as often as a four-stroke at 12,400 RPM. **Adopted mitigations:**

- **~3,000 bar common-rail injection** for faster fuel-air mixing.
- **Two injectors per cylinder,** side-mounted in the liner wall (standard for opposed-piston diesels, which have no head to put an injector in).
- **HVO's high cetane number** (~75–90, versus ~50 for fossil diesel) shortens ignition delay, a genuine benefit of the chosen fuel.
- **Opposed-piston combustion chamber:** No cylinder head means lower heat loss and strong swirl from the uniflow scavenging, both of which speed up combustion.

Mean piston speed is a comfortable ~14 m/s. **Fallback:** if the redline must drop to ~5,500 RPM, keeping 750 hp needs ~19 bar BMEP (≈38 bar four-stroke equivalent), still just under F1 V6 stress levels.

**M2. The boost figures and Audi comparison are off, and "compound" is mislabelled.**

- ~~Audi comparison and 4.5–5.5 bar boost~~ **Resolved:** the Audi Le Mans diesels were regulation-restricted to much lower boost, so the comparison is dropped. At 3.2 L, the engine needs only ~3–3.5 bar gauge (~4–4.5 bar absolute), well within what the two-stage series turbos can deliver.
- ~~"Compound" mislabelled as parallel twin-turbo~~ **Resolved:** true series (compound) turbocharging is adopted, with intercooling between stages.

**M3. The engine architecture contradicts itself.**

- ~~"Flat-4" vs "opposed-piston"~~ **Resolved:** opposed-piston (two pistons sharing each cylinder, two crankshafts, two-stroke, no cylinder heads) is adopted.
- In an opposed-piston engine, the exhaust ports sit at one end of each cylinder, so they're normally all on one side. "One turbo per outer bank" only works if alternate cylinders are flipped, which complicates the crank geartrain. **Resolved:** a single exhaust manifold feeding series (compound) turbos is adopted.
- ~~"3D-printed" vs "billet"~~ **Resolved:** 3D-printed Alloy X block with CNC finish machining (Rule 5 now explicitly counts large-format metal printers as standard equipment).
- Aluminium-lithium loses strength at engine temperatures and is a sheet/plate aerospace alloy, not a block material. Titanium blocks suffer from poor heat conduction and bore galling. **Resolved:** Alloy X, a novel high-temperature light alloy (Rule 5), is adopted for the block, crankcase, crankshafts, and geartrain (see "Engine Block: Alloy X" above and [weight-budget.md](weight-budget.md)).
- An opposed-piston two-stroke has no crankcase pumping, so it needs forced scavenging at all speeds. The e-turbos provide this.

**M4. Fuel load: resolved at ~90 kg (now ~94 kg with the underfloor fans).**
Assuming a ~305 km, ~1.5 h race, with the diesel averaging ~65% of its 560 kW peak at 50% thermal efficiency, burning HVO (~44 MJ/kg): fuel needed ≈ 365 kW × 5,400 s / 0.50 / 44 MJ/kg ≈ **90 kg** (adopted). The original 65–70 kg would have required the diesel to average only ~half its peak power. Displacement doesn't change this, since fuel use follows power output. The underfloor fans later added ~15 kW of average electrical load, ultimately supplied by the diesel, adding ~4 kg ([aero.md](aero.md)).

**M5. Energy store: resolved with a ~45 kg pack.**
The original 25–30 kg store couldn't deliver the electric power: a lithium pack would have needed ~15 kW/kg, and an ultracapacitor would have held only 1–2.5 s of deployment. **Adopted:** electric output is fixed at 450 kW, giving the 55/45 split with the 750 hp diesel, from a ~45 kg high-power lithium pack:

- ~10 kW/kg at pack level, at the top end of current high-power cells.
- ~100 Wh/kg → ~4.5 kWh (~16 MJ) total, run in a ~50% charge window for cell life → ~8 MJ usable, or ~18 s at full power from full charge.
- ~7–8 MJ recovered per lap (braking regen through 450 kW of MGU-K capacity, plus MGU-H harvest), supporting ~15–18 s of full deployment every lap.
- The MGU-H can also feed the MGU-Ks directly, bypassing the pack, when the exhaust has energy to spare.
- Top-speed dependency: on diesel power alone (~515 kW at the wheels), top speed with DRS closed drops to roughly 315 km/h. The 375 km/h figure (and ~400 km/h with DRS) needs electric deployment at the end of the straight, so the energy strategy must save charge for long straights.

**M6. Cooling logic: resolved.**
The original idea closed the louvers on straights, where heat output peaks (~365 kW at full throttle and full deployment). **Adopted:** a temperature-controlled strategy in [cooling.md](cooling.md): three cooling loops, louvers that partly close at high speed only as far as ram airflow allows, predictive pre-cooling using ~1 MJ of thermal buffer before long straights, and the underfloor fans pulling radiator air for low-speed running.

**M7. Exhaust energy contention: partly resolved.**
The blown diffuser has been dropped, leaving the MGU-H turbines and the aftertreatment sharing the exhaust stream. The catalysts need heat while the MGU-H wants to extract it. Placing the aftertreatment between the turbine stages (see [aftertreatment.md](aftertreatment.md)) keeps the catalysts hot and lets the low-pressure turbine harvest what's left.

**M8. The weight budget is tight.**
The design adds two front MGU-Ks with front driveshafts (no differential), SCR + DPF + a urea (AdBlue/DEF) tank, two-stage turbos with intercoolers, and an opposed-piston engine with two crankshafts and a geartrain. Each is a significant addition over a standard F1 car. The re-baselined numbers add more over the original sketch: the battery grows by ~15–20 kg (to ~45 kg), the fuel load by ~20–25 kg (to ~90 kg), and the larger 3.2 L engine adds an estimated ~10–20 kg. **Resolved with a revised target:** the component-level budget in [weight-budget.md](weight-budget.md) comes to ~835 kg (car + driver, no fuel or DEF) after two rounds of cuts totalling ~70 kg: Alloy X across the engine and chassis metal parts (at ~2.7 g/cm³), optimised printed walls, a 6-speed gearbox, and smaller rear brakes. The underfloor fan system (~12 kg net), active suspension (~10 kg net), and load-rated tyres (~5 kg) were then added, giving **~862 kg**. The original ~780–800 kg isn't achievable; the car runs ~94 kg over the 768 kg FIA minimum but keeps ~20% better power-to-weight than F1.

### Minor

All resolved:

- ~~HVO terminology~~ **Resolved:** now described as renewable diesel (paraffinic, hydrotreated), not biodiesel (FAME) or synthetic e-fuel.
- ~~Split vs. numbers~~ **Resolved:** headline figure fixed at ~1,350 hp (560 kW diesel + 450 kW electric), a 55/45 split.
- ~~"Torque wins races"~~ **Resolved:** "How to Win" now argues traction, power band, and power-to-weight. At any road speed, acceleration depends on power at the wheels; gearing converts engine torque freely.
- ~~"Combined system torque" of 1,200+ Nm~~ **Resolved:** removed; adding torques measured on different shafts at different speeds isn't meaningful.
- ~~"Doesn't run out of breath"~~ **Resolved:** top speed is now stated as drag-limited (~375 km/h at CdA ≤ ~1.3 m²) and battery-dependent.
- ~~Diesel "thick walls" premise~~ **Resolved:** reworded; F1 engines already run similar peak pressures, and Alloy X covers the rest.
- ~~Comparison table~~ **Resolved:** labelled as estimates and recalculated. Cornering grip corrected from "5.5+ G": a heavier car with the same downforce has slightly *less* grip, not more. The underfloor fan (added later) restores it: ~4.0 G at 100 km/h, ~5.0 G at 250 km/h.
- ~~Gearing~~ **Resolved:** "long final drive because of torque from idle" replaced with calculated ratios (~8.4:1 to ~2.24:1 over 6 speeds).

### Strengths Worth Keeping

- **Opposed-piston layout (adopted):** No cylinder heads gives a genuinely low engine and centre of gravity, a real aero and handling gain.
- **Front MGU-Ks (now one per wheel):** The front axle does most of the braking, so front regen recovers far more energy than rear-only. AWD traction out of slow corners is also a real advantage.
- **Electrified turbocharging:** Solves the two-stroke scavenging problem and turbo lag in one system.
- **Exploiting no fuel-flow limit:** Valid under the current rules; the gain is real, just smaller than claimed (see M1).
- **HVO fuel:** Besides satisfying Rule 4, its high cetane number directly helps the high-RPM diesel combustion (see M1).

### Suggested Next Steps

1. ~~Choose the hybrid architecture~~ **Done:** parallel hybrid (diesel drives the rear wheels through the gearbox, with one MGU-K per front wheel and a rear MGU-K). A series hybrid was considered and rejected: ~10% conversion losses and an estimated 40–70 kg extra mass outweigh its steady-state engine and full torque-vectoring benefits. The opposed-piston two-stroke and series (compound) e-turbos are adopted, and the aftertreatment sits between turbine stages ([aftertreatment.md](aftertreatment.md)).
2. ~~Re-baseline displacement vs. power, fuel load, and energy store~~ **Done:** 3.2 L / 750 hp diesel, ~90 kg fuel, 450 kW electric from a ~45 kg pack (M1, M4, M5).
3. ~~Build a component-level weight budget~~ **Done:** [weight-budget.md](weight-budget.md), ~862 kg including the fan system, active suspension, and load-rated tyres (M8).
4. ~~Fix the cooling strategy and engine block material/process~~ **Done:** [cooling.md](cooling.md) (M6) and 3D-printed Alloy X block (M3).
5. ~~Draw a layout to set weight distribution~~ **Done (rough):** [layout.md](layout.md): 3.5 m wheelbase, ~45/55 weight split, ~0.31 m CG height.
6. ~~Aero concept~~ **Done:** fan-assisted ground effect with sliding skirts and DRS ([aero.md](aero.md)).
7. ~~Suspension and front packaging~~ **Done:** fully active electromechanical suspension with passive springs ([suspension.md](suspension.md)).
8. ~~Size radiators and inlets~~ **Done:** [cooling.md](cooling.md).
9. ~~Tyre specification and strategy~~ **Done:** W fronts, HD rears, mix-and-match strategy ([tyres.md](tyres.md)).
