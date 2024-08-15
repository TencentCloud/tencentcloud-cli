**Example 1: 例子**



Input: 

```
tccli tandon GetCommonCategoryList --cli-unfold-argument  \
    --VisibleChannel 123 \
    --OwnerUin 123 \
    --PostUin 123 \
    --Area 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Categories": [
                {
                    "Cell": {
                        "Visible": 0,
                        "Weights": 1,
                        "Name": "123",
                        "Description": "123"
                    },
                    "Id": 1,
                    "Children": [
                        {
                            "Cell": {
                                "Name": "123",
                                "Visible": 0,
                                "Weights": 1,
                                "Common": 1,
                                "ImgUrl": "123",
                                "Description": "123"
                            },
                            "Id": 1
                        }
                    ]
                },
                {
                    "Cell": {
                        "Visible": 0,
                        "Weights": 1,
                        "Name": "123",
                        "Description": "123"
                    },
                    "Id": 1,
                    "Children": [
                        {
                            "Cell": {
                                "Description": "123",
                                "Visible": 0,
                                "Weights": 1,
                                "Common": 0,
                                "ImgUrl": "123",
                                "Name": "123"
                            },
                            "Id": 1
                        },
                        {
                            "Cell": {
                                "Name": "123",
                                "Visible": 0,
                                "Weights": 1,
                                "Common": 1,
                                "ImgUrl": "123",
                                "Description": "123"
                            },
                            "Id": 1
                        }
                    ]
                }
            ],
            "BaseCategory": [
                {
                    "ApplyChannel": 0,
                    "CategoryName": "123",
                    "CategoryId": 0,
                    "ParentId": 0
                }
            ]
        },
        "RequestId": "123"
    }
}
```

