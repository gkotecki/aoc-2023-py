use std::fs::read_to_string;

fn main() {
    println!("Parsing day 05 input...");

    let input = read_to_string("days/05/input.txt").expect("error reading filepath");

    let data = input
        .split("\n\n")
        .map(|group| group.lines().collect::<Vec<_>>())
        .inspect(|x| { dbg!(x); })
        .collect::<Vec<_>>();

    let seeds = &data[0][0].split_whitespace().skip(1).collect::<Vec<_>>();

    let seed_to_soil = &data[1].iter().skip(1).collect::<Vec<_>>();
    let soil_to_fertilizer = &data[2].iter().skip(1).collect::<Vec<_>>();
    let fertilizer_to_water = &data[3].iter().skip(1).collect::<Vec<_>>();
    let water_to_light = &data[4].iter().skip(1).collect::<Vec<_>>();
    let light_to_temperature = &data[5].iter().skip(1).collect::<Vec<_>>();
    let temperature_to_humidity = &data[6].iter().skip(1).collect::<Vec<_>>();
    let humidity_to_location = &data[7].iter().skip(1).collect::<Vec<_>>();

    let seed_ranges: Vec<(i64, i64)> = (0..seeds.len())
        .step_by(2)
        .map(|i| {
            let start = seeds[i].parse().unwrap();
            (start, start + seeds[i + 1].parse::<i64>().unwrap())
        })
        .collect();

    let mut smallest_location = 0;
    let total = 60_294_664.0;
    let now = std::time::Instant::now();

    loop {
        if smallest_location % 50_000 == 0 {
            print!("time: {:.2}s   ", now.elapsed().as_secs_f64());
            println!("location: {:.2}%", smallest_location as f64 / &total * 100.0);
        }

        let humidity = find_in(humidity_to_location, smallest_location);
        let temperature = find_in(temperature_to_humidity, humidity);
        let light = find_in(light_to_temperature, temperature);
        let water = find_in(water_to_light, light);
        let fertilizer = find_in(fertilizer_to_water, water);
        let soil = find_in(soil_to_fertilizer, fertilizer);
        let seed = find_in(seed_to_soil, soil);

        if seed_ranges.iter().any(|&(start, end)| start <= seed && seed < end)
        {
            println!("Seed: {}, Location: {}", seed, smallest_location);
            break;
        }

        smallest_location += 1;
    }
}

fn find_in(lines: &Vec<&&str>, value: i64) -> i64 {
    for line in lines {
        let parts: Vec<i64> = line
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        let source_start = parts[0];
        let dest_start = parts[1];
        let size = parts[2];
        if value >= source_start && value <= (source_start + size) {
            return dest_start + (value - source_start);
        }
    }
    return value;
}
