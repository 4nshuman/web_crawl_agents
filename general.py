import os

#Each website crawled is a seperate directory
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("creating project "+directory)
        os.makedirs(directory)

#create queue and crawled files(if not created)
def create_data_files(project_name, base_url):
    queue = project_name+"/queue.txt"
    crawled = project_name+"/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")

#create file function
def write_file(path, data):
    fo = open(path, "w")
    fo.write(data)
    fo.close()

#append file function
def append_file(path, data):
    with open(path, "a") as fo:
        fo.write("\n"+data)

#delete contents of a file
def delete_file(path):
    with file(path,"w") as fo:
        pass

#file to set
def file_to_set(file_name):
    result = set()
    with open(file_name,"rt") as fo:
        for line in fo:
            result.add(line.replace("\n",""))
    return result

#set to file
def set_to_file(links, file_name):
    delete_file(file_name)
    for link in sorted(links):
        append_file(file_name, link)

create_project_dir("something")
create_data_files("something","something.com")
