import json

def load_data():
    try:
        with open('video.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
            return []
    

def save_data_helper(videos):
    with open('video.txt','w') as file:
        json.dump(videos,file)



def add_video(videos):
    Name = input("enter name of video \n")
    time = input(" enter time-duration of video \n")
    videos.append({'name' : Name, 'time': time})
    save_data_helper(videos)


def list_all_videos(videos):

    print("\n")

    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']} Duration:{video['time']}")

    print("\n")    




def update_video(videos):
    list_all_videos(videos)
    index = int(input("enter index no. to update"))
    if 1 <= index <= len(videos):
        name = input("enter new name of video")
        time = input("enter new time duration")
        videos[index-1] = {'name': name , 'time': time}
        save_data_helper(videos)
    else:
        print("index selected is invalid")

    

def delete_video(videos):
        list_all_videos(videos)
        index = int(input("enter index no. to be deleted"))
        if 1 <= index <= len(videos):
            del videos[index-1]
            save_data_helper(videos)
        else:
            print("index selected is invalid")




def main():

    videos = load_data()

    while True:
        print("\n Choose an option to manage your videos")
        print("1. Add a new video")
        print("2. Make a list of all videos")
        print("3. Update the list of videos")
        print("4. Delete a video")
        print("5. Exit")

        Choice = input("enter ur choice .")

        match Choice:
            case '1' :
                 add_video(videos)
                
            case '2' :
                list_all_videos(videos)
                
            case '3' :
                update_video(videos)
            case '4' :
                delete_video(videos)
            case '5' :
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()
