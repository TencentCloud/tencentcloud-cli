**Example 1: 调用成功示例**

调用成功示例

Input: 

```
tccli ocr RecognizeTableMultiOCR --cli-unfold-argument  \
    --ImageUrl https://xxx.com/1.pdf \
    --PdfStartPageNumber 1 \
    --PdfEndPageNumber 2
```

Output: 
```
{
    "Response": {
        "RequestId": "43e5db77-ea0c-4b82-9f77-86387eb856e5",
        "DataBase64": "fCDpobnnm64gfCAyMDI0IOW5tDkg5pyIMz...4LjQ0IHwK"
    }
}
```

