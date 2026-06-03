**Example 1: 查询标注任务列表**



Input: 

```
tccli tione DescribeAnnotatedTaskList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Order DESC \
    --OrderField CreateTime
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TaskList": [
            {
                "TaskId": "373kxtfvtmv4",
                "TaskName": "dwfwf",
                "DatasetId": "373kxtfvtmv4",
                "DatasetName": "分割检测类",
                "SceneName": "Image_Classification",
                "LabelValueList": [
                    {
                        "LabelName": "mockname",
                        "LabelColor": "#FF0000"
                    }
                ],
                "Status": 2,
                "AbnormalMsg": "",
                "IsSubmitting": false,
                "CamTagList": [
                    {
                        "Key": "mockkey",
                        "Value": "mockvalue"
                    }
                ],
                "TaskNote": "",
                "DataSetVersion": "v3",
                "NumAnnotated": 0,
                "NumTotal": 31,
                "CreateTime": 1642504245,
                "OcrToolType": 0,
                "OcrTextAttributeAnnotateEnable": false,
                "ExportFormat": "ANNOTATION_FORMAT_TI",
                "SubmittingErrorMsg": "",
                "OcrAnnotationContentType": 0,
                "EnableAuxiliaryAnnotation": false
            }
        ],
        "RequestId": "d78711c1-02b1-452e-a447-49e402a014a0"
    }
}
```

