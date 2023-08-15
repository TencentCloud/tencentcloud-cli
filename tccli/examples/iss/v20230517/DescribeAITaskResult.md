**Example 1: 失败示例**

AI任务不存在

Input: 

```
tccli iss DescribeAITaskResult --cli-unfold-argument  \
    --TaskId at**********************1 \
    --ChannelId ********************** \
    --DetectType Pet
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.AITaskNotExisted",
            "Message": "AI任务不存在"
        },
        "RequestId": "1bd31583-6bd4-486c-8ae3-1844cf4e6d1e"
    }
}
```

**Example 2: 成功示例**

无

Input: 

```
tccli iss DescribeAITaskResult --cli-unfold-argument  \
    --TaskId at**********************8 \
    --ChannelId ********************** \
    --DetectType Pet
```

Output: 
```
{
    "Response": {
        "Data": {
            "AIResults": {
                "Body": null,
                "Car": null,
                "ChefCloth": null,
                "ChefHat": null,
                "FaceMask": null,
                "Pet": [
                    {
                        "PetInfo": [
                            {
                                "Location": {
                                    "Height": 854,
                                    "Width": 1142,
                                    "X": 567,
                                    "Y": 87
                                },
                                "Name": "dog",
                                "Score": 91
                            }
                        ],
                        "Time": "0.000000",
                        "Url": "https://****************************************************"
                    }
                ],
                "PhoneCall": null,
                "Smoking": null
            },
            "TaskId": "at**********************8"
        },
        "RequestId": "45e68b99-dec9-46f4-81e7-bc4a3c768536",
        "TotalCount": 1
    }
}
```

