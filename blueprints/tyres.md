# Tyres

Tyre specification and strategy for the ScuderiaTroll ST67. All figures are design estimates for a fictional vehicle; mass and loads come from [weight-budget.md](weight-budget.md), [aero.md](aero.md), and [suspension.md](suspension.md).

## Rules That Apply

- **Sporting Rule 17 (Tyre Supply):** Single control supplier; five compounds (Soft, Medium, Hard, Intermediate, Full Wet); a catalogue of standard sizes and load ratings; one size per axle, declared before each event.
- **Sporting Rule 2:** Compounds can be mixed and matched across all wheels. Hard limit of 3 swaps per race; tyre changes, map changes, and some repairs share it.
- **Sporting Rule 3:** Switching onto Full Wets and/or the wet map is free; switching off counts as one swap.
- **Technical Rule 3:** Outer tyre faces must stay within the 2.0 m width.

## Supplier Catalogue (Assumed)

All sizes on 18-inch rims with ~0.72 m overall diameter. Ratings are peak dynamic vertical load per tyre.

| Size | Width | Peak load rating | Typical use |
| --- | --- | --- | --- |
| N (Narrow) | 280 mm | 9 kN | Light cars; inner wheels on 5–6 wheel cars |
| S (Standard) | 305 mm | 11 kN | F1-like front axle |
| W (Wide) | 380 mm | 12.5 kN | F1-like rear axle; driven front axles |
| HD (Heavy-duty wide) | 405 mm | 15 kN | Heavy or high-downforce cars; reinforced carcass (~+1.5 kg per tyre) |

## Our Loads

Peak per-tyre loads at race start (~960 kg), with the downforce capped at ~21 kN and ~5 G cornering:

| Case | Front outer tyre | Rear outer tyre |
| --- | --- | --- |
| Fast corner (300 km/h, ~5.2 G) | ~10.9 kN | **~13.4 kN** |
| Straight-line braking from 300 km/h | ~8.9 kN | ~6.3 kN |
| F1 rear, fast corner (same method) | — | ~11.3 kN |

Method: total vertical load (weight + downforce) split ~45/55 front/rear, plus lateral load transfer (mass × lateral g × CG height / track width, ~9 kN total at 5 G with a 0.31 m CG and ~1.6 m track), shared ~45/55.

## Our Selection

| Axle | Size | Load margin | Why |
| --- | --- | --- | --- |
| **Front** | **W (380 mm)** | ~13% (12.5 vs ~10.9 kN) | S (11 kN) would be at its limit. Wider fronts also suit AWD traction, front regen braking, and torque vectoring |
| **Rear** | **HD (405 mm)** | ~12% (15 vs ~13.4 kN) | W (12.5 kN) is below the ~13.4 kN peak |

Active suspension's tyre-load management trims peaks further, adding margin.

**Packaging:** To keep outer faces within the 2.0 m width, wheel centres move inboard: front track ~1.62 m, rear ~1.60 m (centre to centre).

**Mass:** Wider fronts (+~1 kg each) and heavy-duty rears (+~1.5 kg each) add **~5 kg**, taking wheels and tyres from 76 to 81 kg and the car to **~862 kg** (see [weight-budget.md](weight-budget.md)).

## Strategy

### Mix and Match

Mixing compounds across wheels (Sporting Rule 2) lets each tyre run the compound its workload suits:

- **Circuit direction:** On a mostly clockwise circuit, the left-side tyres are the outside tyres in most corners and carry the peak loads. Run a harder compound on the left side and a softer one on the right (reverse for anti-clockwise circuits).
- **Axle workload:** The rears carry ~55% of the load plus the diesel's drive; the fronts carry braking, front-motor drive, regen, and steering. Which axle degrades faster depends on the circuit:
  - **Traction-limited circuits** (many slow corners): harder rears.
  - **Braking-heavy circuits** (long straights into hairpins): harder fronts.
- **Underfloor fan effect:** The fan's speed-independent downforce loads the tyres hard even in slow corners, so slow-corner-heavy circuits will wear tyres faster than on an F1 car. Expect to lean harder there.

### Swaps

With 3 swaps shared between tyres, map changes, and some repairs:

- **Plan 1–2 tyre stops,** keeping at least one swap spare for damage or weather.
- **Bundle work:** Fit fresh skirt wear strips during a tyre stop, where the same swap covers both (Sporting Rule 2).
- **Map changes cost an extra swap** even during a tyre stop, so set the race map to last the whole race where possible.

### Wet Weather

- **Free switch onto wets:** Switching onto Full Wets and the wet map together is free (Sporting Rule 3); switching off both costs one swap.
- **Fan advantage:** The underfloor fan's downforce doesn't depend on speed, so the car keeps grip in slow wet corners where wing cars lose most. This is the car's biggest wet-weather strength.
- **Fan water handling:** The fans will ingest spray from under the floor, so fan motors and inverters need waterproof sealing. The upward-angled exhaust throws extra spray, which is accepted: all cars throw spray, and closed cockpits are an option (Technical Rule 6).
- **Intermediates** count as normal tyre changes.

### Tyre Blankets

Allowed up to a supplier-set temperature cap per compound (Sporting Rule 17), so fresh tyres start partly warm but still need some out-lap work to reach full operating temperature. The car warms tyres quickly: fan downforce loads them even at low speed, AWD works the fronts, and active suspension can load the tyres on the out-lap. That shortens the slow out-lap after each stop.

## Decisions

- **Tyre blankets:** Allowed, with a supplier-set temperature cap per compound.

- **Wet-weather spray from the fans:** Accepted; no rule or design limit needed.
