fn product(x: u32, y: u32) -> u32 {
    return x * y;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_product() {
        let result = product(2, 2);
        assert_eq!(result, 4);
    }
}
