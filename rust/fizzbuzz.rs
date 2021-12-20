fn main() {
    fizzbuzz(15);
}

fn fizzbuzz(n: i32) {
    for number in (1..n+1) {
        let mut statement = String::from("");
        let mut divisible_test = |i, d, s| if i % d == 0 {
            statement.push_str(s)
        };

        divisible_test(number, 3, "Fizz");
        divisible_test(number, 5, "Buzz");

        println!("{}: {}", number, statement);
    }
}

fn fizzbuzzOld(n: i32) {
    let mut index = 1;

    loop {
        let mut statement = String::from("");

        if index % 3 == 0 {
            statement.push_str("Fizz");
        }

        if index % 5 == 0 {
            statement.push_str("Buzz");
        }

        println!("{}: {}", index, statement);

        if index == n {
            break;
        }

        index += 1;
    }
}
