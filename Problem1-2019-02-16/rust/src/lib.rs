use std::collections::HashMap;

pub fn list_sum_checker(num_list: Vec<i32>, target_num: i32) -> bool {
    let mut seen_numbers = HashMap::new();
    for num in num_list {
        let diff = target_num - num;

        let found = match seen_numbers.get(&diff) {
            Some(_i) => true,
            None => false,
        };

        if found {
            return true;
        }

        seen_numbers.entry(num).or_insert(num);
    }
    return false;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_list_sum_checker_valid() {
        let k = 17;
        let num_list = vec![10, 15, 3, 7];
        assert_eq!(list_sum_checker(num_list, k), true);
    }
    
    #[test]
    fn test_list_sum_checker_invalid() {
        let k = 17;
        let num_list = vec![10, 15, 3, 27];
        assert_eq!(list_sum_checker(num_list, k), false);
    }
}
