**Example 1: 查询数据集列表**



Input: 

```
tccli tione DescribeDatasets --cli-unfold-argument  \
    --DatasetIds ds-c4lbz9gg
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DatasetIdNums": 1,
        "DatasetGroups": [
            {
                "DatasetId": "ds-c4lbz9gg",
                "DatasetName": "test",
                "Creator": "100007955047",
                "DatasetVersion": "v1",
                "DatasetType": "TYPE_DATASET_TEXT",
                "DatasetTags": [],
                "DatasetAnnotationTaskName": "",
                "DatasetAnnotationTaskId": "",
                "Process": 100,
                "DatasetStatus": "STATUS_DATASET_SUCCESS",
                "ErrorMsg": "",
                "CreateTime": "2022-01-15 15:01:57",
                "UpdateTime": "2022-01-15 15:01:57",
                "ExternalTaskType": "",
                "DatasetSize": "11.06 M",
                "FileNum": 4,
                "StorageDataPath": {
                    "Bucket": "test-gz-1256580188",
                    "Region": "ap-guangzhou",
                    "Paths": [
                        "train-dataset/"
                    ]
                },
                "StorageLabelPath": {
                    "Bucket": "test-gz-1256580188",
                    "Region": "ap-guangzhou",
                    "Paths": [
                        "train-output/"
                    ]
                },
                "AnnotationStatus": "STATUS_NON_ANNOTATED",
                "AnnotationType": "",
                "AnnotationFormat": "",
                "DatasetVersions": []
            }
        ],
        "RequestId": "f015eab9-1feb-4b1d-8ea0-85fff5b4ddc7"
    }
}
```

