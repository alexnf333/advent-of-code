use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};
use std::time::Instant;
#[macro_use(c)]
extern crate cute;
use std::collections::HashSet;
use std::f64::consts::PI;

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

// asteroids_in_sight() returns number of asteroids in sight and a vector with
// asteroid information and destruction order
fn asteroids_in_sight(map: &Vec<Vec<char>>, ref_y: usize, ref_x: usize)
                        -> (usize, Vec<(f64, f64, usize, usize)>) {
    let ref_y = ref_y as isize;
    let ref_x = ref_x as isize;
    let mut angles_set = HashSet::new();
    let mut destruction_order: Vec<(f64, f64, usize, usize)> = Vec::new();
    for y in 0..map.len() {
        for x in 0..map[y].len() {
            let x_i = x as isize;
            let y_i = y as isize;
            if ref_x == x_i && ref_y == y_i {
                continue;
            } else if map[y][x].to_string() == "#".to_string() {
                let y1 = (ref_y-y_i) as f64;
                let y2 = 1 as f64;
                let mut angle = y1.atan2((ref_x-x_i) as f64) - y2.atan2(0 as f64);
                let angle_str = angle.to_string();
                angles_set.insert(angle_str);
                if angle < 0.0 {
                    angle = 2.0 * PI - angle.abs();
                }
                let distance = ((ref_x-x_i)*(ref_x-x_i) + (ref_y-y_i)*(ref_y-y_i)) as f64;
                let distance = distance.sqrt();
                destruction_order.push((angle, distance, x, y));
            }
        }
    }
    (angles_set.len(), destruction_order)
}
// asteroids() determines asteroids in sight from best location and the 200th
// destroyed asteroid
fn asteroids() -> f64 {
    let mut map: Vec<Vec<char>> = Vec::new();
    let mut max_asteroids = 0;
    let mut max_destruction = Vec::new();
    let now = Instant::now();

    let space = lines_from_file("data.txt");
    for asteroids in space {
        let char_vec:Vec<char> = asteroids.chars().collect();
        map.push(char_vec);
    }

    for y in 0..map.len() {
        for x in 0..map[y].len() {
            if map[y][x].to_string() == "#".to_string() {
                let (xy_asteroids, xy_destruction) = asteroids_in_sight(&map, x, y);
                if xy_asteroids > max_asteroids {
                    max_asteroids = xy_asteroids;
                    max_destruction = xy_destruction;
                }
            }
        }
    }
    println!("Maximum asteroids in sight: {}", max_asteroids);
    max_destruction.sort_by(|a, b| a.partial_cmp(b).unwrap());

    let mut destroyed_asteroids = 0;
    let mut angle_index = 0;
    let mut next_angle = 1;

    loop {
        while max_destruction[angle_index].0 == max_destruction[next_angle].0 {
            next_angle = next_angle + 1;
            if next_angle >= max_destruction.len() {
                angle_index = 0;
                next_angle = 0;
            }
        }
        if destroyed_asteroids == 199 {
            println!("200th asteroid result: {}",
                        max_destruction[angle_index].2 * 100
                        + max_destruction[angle_index].3);
            break;
        }
        max_destruction.remove(angle_index);
        destroyed_asteroids = destroyed_asteroids + 1;
        angle_index = next_angle - 1;
        if next_angle >= max_destruction.len() {
            angle_index = 0;
            next_angle = 1;
        }
    }

    let new_now = Instant::now();
    let elapsed_time = new_now.duration_since(now).as_millis() as f64;
    println!("elapsed time: {} milliseconds", elapsed_time);
    elapsed_time
}

// calculate average proccesing time for the indicated number of tests
fn main() {
    const NUMBER_OF_TESTS: u8 = 100;
    let tests_array = c![asteroids(), for _x in 0..NUMBER_OF_TESTS];
    let sum: f64 = tests_array.iter().sum();
    println!("average time: {} milliseconds", sum / NUMBER_OF_TESTS as f64);
}
