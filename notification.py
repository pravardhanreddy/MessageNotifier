import cv2
import numpy as np
import pyautogui
from time import sleep
from twilio.rest import Client

WHITE = np.array([242, 242, 242])
GREY = np.array([17, 15, 17])
MID1 = np.array([53, 50, 51])
MID2 = np.array([17, 16, 15])
MID3 = np.array([18, 15, 16])

account_sid = 'ACbbaeb9dc5610170bc823e5e1079dfe17'
auth_token = 'df370b59e9ddc386b7d93e08dfd458b2'
client = Client(account_sid, auth_token)


i = 0
while True:
    sleep(1)
    i += 1
    img = pyautogui.screenshot()
    frame = np.array(img)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    sub = frame[728:764, 200:240, :]
    # print("Frame shape: ", frame.shape)
    # print("Sub shape: ", sub.shape)
    print("Pixel Value: ", frame[756, 206])

    # print(type(frame[756,206]))
    # print(type(WHITE))

    if(np.array_equal(frame[756, 206], WHITE) or
       np.array_equal(frame[756, 206], GREY) or
       np.array_equal(frame[756, 206], MID1) or
       np.array_equal(frame[756, 206], MID2) or
       np.array_equal(frame[756, 206], MID3) or
       (frame[756,206,0] == frame[756,206,1] and
        frame[756,206,0] == frame[756,206,2]) or
       (frame[756,206,0] < 80 and
        frame[756,206,1] < 80 and
        frame[756,206,2] < 80 )):
        print("Normal")
    else:
        
        print("Received a msg")
        call=client.calls.create(
            twiml = '<Response><Say>You have a message</Say></Response>',
            to = '+917002863704',
            from_ = '+18312563857'
        )
        sleep(100)

    # cv2.imshow("show", frame)
    # cv2.imshow("crop", sub)
    # cv2.imwrite("test" + str(i) + ".png",frame)
    # cv2.imwrite("crop" + str(i) + ".png",sub)

    # if cv2.waitKey(10000) == ord('q'):
        # break

# cv2.destroyAllWindows()
