* `wget https://dumps.wikimedia.org/other/cirrussearch/20180430/thwiki-20180430-cirrussearch-content.json.gz` 
* `zcat thwiki-20180430-cirrussearch-content.json.gz | jq -r .text | grep -v > thai_wiki.txt`
