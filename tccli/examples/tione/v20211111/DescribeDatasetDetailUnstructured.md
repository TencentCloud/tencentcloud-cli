**Example 1: 查询非结构化数据集详情**



Input: 

```
tccli tione DescribeDatasetDetailUnstructured --cli-unfold-argument  \
    --Limit 10 \
    --AnnotationStatus STATUS_ALL \
    --DatasetIds ds-wxz4x99g \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AnnotatedTotalCount": 1,
        "NonAnnotatedTotalCount": 0,
        "FilterTotalCount": 1,
        "FilterLabelList": [
            {
                "DatasetId": "ds-wxz4x99g",
                "FileId": "aab4904b30948ed59c7cbae36dcaf448",
                "FileName": "2007_000032.jpg",
                "ClassificationLabels": [
                    "ddd"
                ],
                "DetectionLabels": [],
                "SegmentationLabels": [],
                "RGBPath": "",
                "LabelTemplateType": "LABEL_TYPE_CLASSIFICATION",
                "DownloadUrl": "https://test-gz-1256580188.cos.ap-guangzhou.myqcloud.com/dataset/2007_000032.jpg?x-cos-security-token=a45oSsBOUyhc3KRpQFDXlcR3BlGyDkva4403718b4da01693bf46d2f1f5e87fc3TS_hyxhQz-QNlu4x7gaYiRFiyaCwZ8YLchECAsWuq2YwQLjLgH6XNCC4z0j824Vq_NuRzMox-AxLkefKqqqPRgjJOTgNtsnEkv56uwIGl5WDmhx9uwjkk5eX6YYcaxPMGat6s9ChRFxGuZJ_j1cQamP4ry4wi_JZaiiCt_R_KwgE7t1lA8LIZCjZ06--lHc5yJDjpp2lESU3NROHwLdflPduzY6Q6LqVmDsoU6sErIhw9UBtJJtmNkwqsx29b981YstlClTkl4WKcLo7mTzZ_yCxRxmwTSR0FnnU6o8h_NM7ELcUwUdVVESh0CUoNEuz8UY3ugl5NUFLSd2XfL6fEBLsN8nJVmZwSnrWZXUw--0&q-sign-algorithm=sha1&q-ak=AKID-VyRdLwBsnzR-yVO3kfSyiioEfa49eVB3cO657BeKiIZ-V7asNiXirle2ttvuD9N&q-sign-time=1642506246%3B1642509846&q-key-time=1642506246%3B1642509846&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=aa525ef914ee202a342f4f5f9c2676e3abebe3f9",
                "DownloadThumbnailUrl": "https://test-gz-1256580188.cos.ap-guangzhou.myqcloud.com/dataset/2007_000032.jpg?x-cos-security-token=a45oSsBOUyhc3KRpQFDXlcR3BlGyDkva4403718b4da01693bf46d2f1f5e87fc3TS_hyxhQz-QNlu4x7gaYiRFiyaCwZ8YLchECAsWuq2YwQLjLgH6XNCC4z0j824Vq_NuRzMox-AxLkefKqqqPRgjJOTgNtsnEkv56uwIGl5WDmhx9uwjkk5eX6YYcaxPMGat6s9ChRFxGuZJ_j1cQamP4ry4wi_JZaiiCt_R_KwgE7t1lA8LIZCjZ06--lHc5yJDjpp2lESU3NROHwLdflPduzY6Q6LqVmDsoU6sErIhw9UBtJJtmNkwqsx29b981YstlClTkl4WKcLo7mTzZ_yCxRxmwTSR0FnnU6o8h_NM7ELcUwUdVVESh0CUoNEuz8UY3ugl5NUFLSd2XfL6fEBLsN8nJVmZwSnrWZXUw--0&q-sign-algorithm=sha1&q-ak=AKID-VyRdLwBsnzR-yVO3kfSyiioEfa49eVB3cO657BeKiIZ-V7asNiXirle2ttvuD9N&q-sign-time=1642506246%3B1642509846&q-key-time=1642506246%3B1642509846&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=aa525ef914ee202a342f4f5f9c2676e3abebe3f9&imageView2/2/w/256/h/256",
                "DownloadRGBUrl": ""
            }
        ],
        "RequestId": "db00dce1-5cb9-4072-96ce-24ce2433f21c",
        "RowTexts": []
    }
}
```

