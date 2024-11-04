school_id = { 'id1' : {'Name ': 'Sara', 'class': 'grade 9', 'subject': ['math' , 'english' , 'science']}
                       , 'id2' : {'Name ': 'Sam', 'class': 'grade 9', 'subject': ['math' , 'english' , 'science']}
                       , 'id3' : {'Name ': 'Ahmed', 'class': 'grade 9', 'subject': ['math' , 'english' , 'science']},
                       'id4': {'Name ': 'Sara', 'class': 'grade 9', 'subject': ['math' , 'english' , 'science']}
}



results = {}
for key,value in school_id.items():
    if value not in results.values():
        results[key] = value

print(results)