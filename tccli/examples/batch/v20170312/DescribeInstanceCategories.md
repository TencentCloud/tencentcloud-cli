**Example 1: Querying Instance Category Information**

Query the category and category details of the current CVM instance family.

Input: 

```
tccli batch DescribeInstanceCategories --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceCategorySet": [
            {
                "InstanceFamilySet": [
                    "C3",
                    "CN3"
                ],
                "InstanceCategory": "COMPUTE_3"
            },
            {
                "InstanceFamilySet": [
                    "C2"
                ],
                "InstanceCategory": "COMPUTE_2"
            },
            {
                "InstanceFamilySet": [
                    "S2",
                    "S2ne",
                    "I2",
                    "D1",
                    "M2"
                ],
                "InstanceCategory": "GENERAL_2"
            },
            {
                "InstanceFamilySet": [
                    "S3",
                    "SN3ne",
                    "S4",
                    "I3",
                    "M3",
                    "M4"
                ],
                "InstanceCategory": "GENERAL_3"
            }
        ],
        "RequestId": "166a2a24-888f-4fd5-82ef-f41e4754d994"
    }
}
```

