use std::collections::HashSet;

pub fn first_positive_missing_integer(list_in: Vec<i32>) -> i32 {
    let mut seen = HashSet::new();
    let mut largest_number = 0;
    let mut missing_number = 0;
    for number in list_in {
        if number < 0 {
           continue
        }
        seen.insert(number);
        let next_number = number + 1;

        if number > largest_number {
            largest_number = number;
        }

        if missing_number == 0 {
            missing_number = next_number;
        }

        if !seen.contains(&next_number) && missing_number > next_number {
            missing_number = next_number;
        }

        if seen.contains(&missing_number) {
           missing_number = next_number;
        }
    }

    if largest_number == missing_number {
        missing_number = missing_number + 1;
    }

    return missing_number
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_first_positive_missing_integer_example_one() {
        let list_in = vec![3, 4, -1, 1];
        let expected_value = 2;

        let actual_value = first_positive_missing_integer(list_in);
        assert_eq!(actual_value, expected_value);
    }

    #[test]
    fn test_first_positive_missing_integer_example_two() {
        let list_in = vec![1, 2, 0];
        let expected_value = 3;

        let actual_value = first_positive_missing_integer(list_in);
        assert_eq!(actual_value, expected_value);
    }

    #[test]
    fn test_first_positive_missing_integer_example_three() {
        let list_in = vec![2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, -1, 1];
        let expected_value = 14;

        let actual_value = first_positive_missing_integer(list_in);
        assert_eq!(actual_value, expected_value);
    }
}
