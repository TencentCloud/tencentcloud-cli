**Example 1: 请求子任务错误日志**



Input: 

```
tccli omics GetRunJobLog --cli-unfold-argument  \
    --RunUuid f9dfef5d-b5a2-4668-bf76-239a022e485d \
    --JobId plan-prophetic-reed-camel-685183 \
    --LogType stderr \
    --ProjectId prj-legal-cyan-goat-888314
```

Output: 
```
{
    "Response": {
        "Content": "Read1 before filtering:\ntotal reads: 10000\ntotal bases: 2500000\nQ20 bases: 2317180(92.6872%)\nQ30 bases: 2133255(85.3302%)\n\nRead2 before filtering:\ntotal reads: 10000\ntotal bases: 2500000\nQ20 bases: 1562112(62.4845%)\nQ30 bases: 1313508(52.5403%)\n\nRead1 after filtering:\ntotal reads: 7245\ntotal bases: 1756762\nQ20 bases: 1712864(97.5012%)\nQ30 bases: 1611609(91.7375%)\n\nRead2 after filtering:\ntotal reads: 7245\ntotal bases: 1756762\nQ20 bases: 1319667(75.1193%)\nQ30 bases: 1131274(64.3954%)\n\nFiltering result:\nreads passed filter: 14490\nreads failed due to low quality: 5506\nreads failed due to too many N: 4\nreads failed due to too short: 0\nreads with adapter trimmed: 1632\nbases trimmed due to adapters: 112016\n\nDuplication rate: 0%\n\nInsert size peak (evaluated by paired-end reads): 204\n\nJSON report: fastp.json\nHTML report: fastp.html\n\nfastp --in1 /vol-8ntc8hn8/env/menv-u0sc501i/execution/FastpDemo/f9dfef5d-b5a2-4668-bf76-239a022e485d/call-RunFastp/inputs/vol-8ntc8hn8/cache/gatk-testdata-1252949230/wgs_fastq/NA12878_20k/H06HDADXX130110.1.ATCACGAT.20k_reads_1.fastq --in2 /vol-8ntc8hn8/env/menv-u0sc501i/execution/FastpDemo/f9dfef5d-b5a2-4668-bf76-239a022e485d/call-RunFastp/inputs/vol-8ntc8hn8/cache/gatk-testdata-1252949230/wgs_fastq/NA12878_20k/H06HDADXX130110.1.ATCACGAT.20k_reads_2.fastq --out1 clean-H06HDADXX130110.1.ATCACGAT.20k_reads_1.fastq --out2 clean-H06HDADXX130110.1.ATCACGAT.20k_reads_2.fastq --json fastp.json --html fastp.html --report_title fastp report \nfastp v0.23.2, time used: 1 seconds\n",
        "RequestId": "62c01f22-039d-4c08-8ef1-2adec191a6a2"
    }
}
```

