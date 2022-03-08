import json
from json import JSONDecodeError
from datetime import datetime
import argparse
import pytz


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--src_file', help='the file should be a json file')
    parser.add_argument('-o', '--out_file', help='the file should be a json file')
    args = parser.parse_args()
    return (args.src_file, args.out_file)

def main(src_file, out_file):
    
#Any lines that contain invalid JSON dictionaries should be ignored.
    file = src_file
    d = []

    with open(file, 'r') as f:
        for line in f:
            try:
                w = json.loads(line)
                #Remove all the posts that don’t have a title or title_text field.
                if not ("title" in w or "title_text" in w):
                    raise ValueError    
                
                    #For objects with a “title_text” field, it should be renamed in the output object to “title”
                if "title_text" in w : 
                    w["title"] = w["title_text"]
                    w.pop("title_text")

                date_time_str = w['createdAt']
                date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S%z')
                w['createdAt'] = date_time_obj.astimezone(pytz.utc).strftime('%Y-%m-%dT%H:%M:%S%z')

                if(w["author"] == "" or w["author"] == "N/A"):
                    raise ValueError
                
                if "total_count" in w:
                    if(not((type(w["total_count"]) is str) or (type(w["total_count"]) is int) or (type(w["total_count"]) is float))):
                        raise ValueError
                
                    w["total_count"] = int(w["total_count"])

                builder = []
                if "tags" in w:
                    for s in w["tags"]:
                        builder += s.split(" ")
                
                w["tags"] = builder

                d.append(w)
            except JSONDecodeError:
                pass

            except ValueError:
                pass

    with open(out_file, 'w') as outfile:
        for x in d:
            json.dump(x, outfile)
            outfile.write("\n")
    
if __name__ == "__main__":
    main(*parse_args())