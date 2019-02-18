use std::vec::Vec;

pub fn product_of_vec_except_at_index(list_in: Vec<u32>) -> Vec<u32> {
    let mut list_out = Vec::new();
    for index in 0..list_in.len() {
        let mut list_in_without_index = vec![];
        list_in_without_index.extend_from_slice(&list_in[..index]);
        list_in_without_index.extend_from_slice(&list_in[(index + 1)..]);

        let product = list_in_without_index.iter().product();
        list_out.push(product);
    }

    return list_out;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_product() {
        let list_in = vec![1, 2, 3, 4, 5];
        let expected_out = vec![120, 60, 40, 30, 24];

        let list_out = product_of_vec_except_at_index(list_in);
        assert_eq!(list_out, expected_out);
    }
}
