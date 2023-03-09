import os
import sys

import cv2

pw = "Teodoor"  # Default Password
count = 0


def goto(line_num):
    global line
    line = line_num


line = 1

dir_to_lock = r"D:\folder lock\Locker\folder_to_lock\image.jpeg"  # Enter Directory where folder to be locked is present
dir_to_lock.replace('\\', '/')
dir_to_lock.replace(' ', '_')

folder_to_lock = "Lock_It"  # Name of folder to be locked

run = True
while run:
    v = 0
    pw1 = input("Enter password here: ")
    v = v + 1

    if pw1 == pw:
        os.chdir(dir_to_lock)
        # print("Your path Successfully Changed")

        if not os.path.exists(dir_to_lock + "/" + folder_to_lock):

            if not os.path.exists(f"{folder_to_lock}" + ".{645ff040-5081-101b-9f08-00aa002f954e}"):

                os.mkdir(folder_to_lock)

                print("\nFolder Successfully Locked")

            else:

                os.popen(f'attrib -h -s -r {folder_to_lock}')

                os.rename(f"{folder_to_lock}" + ".{645ff040-5081-101b-9f08-00aa002f954e}", folder_to_lock)

                print("\nFolder has been Successfully Unlocked")

                sys.exit()

        else:

            os.rename(folder_to_lock, f"{folder_to_lock}" + ".{645ff040-5081-101b-9f08-00aa002f954e}")

            os.popen(f'attrib +h +s +r {folder_to_lock}' + '.{645ff040-5081-101b-9f08-00aa002f954e}')

            print("\nFolder has been successfully locked")

            sys.exit()

    else:
        count = count + 1
        print("Wrong Password! Please re-enter the password")
        print(count)

        if count < 3:
            goto(1)

        elif count == 3:
            videoCaptureObject = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            result = True
            while result:
                ret, frame = videoCaptureObject.read()
                dir_to_lock.replace('/', '\\')
                save_to = r"D:\folder lock\Locker\folder_to_lock\image.jpeg"
                save_to.replace('\\', '/')
                cv2.imwrite(save_to + "\\image.jpg", frame)

                result = False
                videoCaptureObject.release()
                cv2.destroyAllWindows()
                run = False
            break
