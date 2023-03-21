**Example 1: 数学公式识别示例代码**

数学公式识别示例代码

Input: 

```
tccli ocr FormulaOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "FormulaInfos": [
            {
                "DetectedText": "\\left\\lbrace\\begin{array}{l} { ( 3 - a ) x - 6 , x \\leq 1 0 , } \\\\ { a ^ { x - 9 } , x > 1 0 } , \\end{array}\\right.  "
            }
        ],
        "RequestId": "b233cdb8-e24f-4670-89a8-aa33d3d341e1"
    }
}
```

