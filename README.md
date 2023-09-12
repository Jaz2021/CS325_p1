# Software Engineering Project 1

Software Engineering Project 1 is an example project meant to scrape a website and output the html into a file

## Installation and Usage
1. Create a new conda environment, ex:
```bash
conda create --name web_scraper python
```
2. Activate your new conda environment
```bash
conda activate web_scraper
```
3. Update your new environment with the requirments.yml:
```bash
conda env update --file ./requirments.yml --prune
```
4. Run main.py through python using the following syntax:
```bash
python ./main.py {website link, default google.com}
```