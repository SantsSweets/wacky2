from PyQt6.QtWidgets import *
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl, QSize
from wacky1 import *
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtMultimedia import QAudioOutput
from PyQt6.QtWidgets import QVBoxLayout

class WackyWatch(QMainWindow, Ui_Widget):
    def __init__(self) -> None:
        """sets up the main window ui and the start-up sounds, it gets the Qsoundeffect function and
        then connects the source of the audio, sets the volume, then plays the sound effect when the application is started."""
        super().__init__()
        self.setupUi(self)
        self.start_sound = QSoundEffect()
        self.start_sound.setSource(QUrl.fromLocalFile('DING.wav'))
        self.start_sound.setVolume(0.6)
        self.start_sound.play()
        """it then sets the video selection buttons to false and hides them until its time to use them after the yes button
        is pressed."""
        self.Vid1.setEnabled(False)
        self.Vid2.setEnabled(False)
        self.Vid3.setEnabled(False)
        self.Vid1.hide()
        self.Vid2.hide()
        self.Vid3.hide()

        '''hides and moves the Video Widget container to the back 
        so that the user can press the buttons that are behind it.'''
        self.VideoContainer.hide()
        self.VideoContainer.lower()
        '''this sets up the Q Media player engine and the Widget where
        the video will play'''
        self.Vid = QMediaPlayer()
        self.VidW = QVideoWidget()
        '''This sets up the audio engine and ties it into the video player so
        that any sound that plays from the video '''
        self.audio = QAudioOutput()
        self.Vid.setAudioOutput(self.audio)
        '''This connects the Layout of the video, with the empty widget that i added
        into the wackywatch ui, it then connects that with the Video widget so that 
        the video will be played in that widget'''
        self.VideoLayout = QVBoxLayout(self.VideoContainer)
        self.VideoLayout.addWidget(self.VidW)
        """this connects all of the buttons with their functions also disables the yes and no buttons
        until the submit button is pressed"""
        self.Confirm.clicked.connect(self.submit)
        self.Yes.clicked.connect(self.acceptname)
        self.N.clicked.connect(self.rejectname)
        self.Yes.setDisabled(True)
        self.N.setDisabled(True)
        """this also connects the 3 video buttons to their respective video playing functions
        this also connects the vid player to the function handle media status that checks if the video is done playing
        it also sets the Clearance to false, so until the first part of the program where you input your name is done
        the program wont proceed with the video playing part of the program."""
        self.Vid1.clicked.connect(self.video1)
        self.Vid2.clicked.connect(self.video2)
        self.Vid3.clicked.connect(self.video3)
        self.Vid.mediaStatusChanged.connect(self.handlemediastatus)
        self.Clearance = False

    def namecheck(self) -> str:
        """checks if line edit is empty or not itll then go into into two different
        functions depending on what button you press it also checks if the name is left as blank
        if it is, then it returns none otherwise it returns the users name
        """
        name = self.YOURNAME.text().strip()
        if name == '':
            self.Question.setText("Enter A REAL NAME!")
            return ''
        return name
    def acceptname(self) -> None:
        """this is the yes button and if the name is left blank then it doesnt continue until the
        name is filled in
        it then deletes the line edit if the name is accepted and it gets rid of the
        question text box and sets up the
        wacky watches users name.
        it then sets the clearance for the video watching to true and goes
        through the if statement
        and goes into the video select function"""
        name = self.YOURNAME.text().strip()
        if name == '':
            return
        self.PP.setText(f"{name}'s WackyWatch")
        self.YOURNAME.deleteLater()
        self.Question.deleteLater()
        self.Clearance = True
        if self.Clearance:
            self.videoselect()
        else:
            pass
    def rejectname(self) -> None:
        """if the no button is selected, then a sound effect is played, it sets the text to
        asking the user to enter their
        name again, then it clears the textbox, and then
        runs the initializes the beginning again."""
        self.Sad_sound = QSoundEffect()
        self.Sad_sound.setSource(QUrl.fromLocalFile('SAD.wav'))
        self.Sad_sound.setVolume(0.2)
        self.Sad_sound.play()
        self.Question.setText("Enter your name again:")
        self.YOURNAME.clear()
        self.Yes.setDisabled(True)
        self.N.setDisabled(True)

    def videoselect(self) -> None:
        """this video select function that runs when the name is accepted enables and show the buttons to be pressed."""
        self.Vid1.setEnabled(True)
        self.Vid2.setEnabled(True)
        self.Vid3.setEnabled(True)
        self.Vid1.show()
        self.Vid2.show()
        self.Vid3.show()

    def video1(self) -> None:
        """these video playing functions set up the video output
        source which is the vidw variable that
        is connected to our VideoContainer widget that we had made in
        QtCreator. it then chooses the video to be played
        and then pyqt6 offers the ability to edit widgets inside of ide
        so i just looked up a guide on how to trim the corners
        on of the widget i repeated this for the next two video playing functions"""
        self.Vid.setVideoOutput(self.VidW)
        self.Vid.setSource(QUrl.fromLocalFile('EP8.mp4'))
        self.VideoContainer.setStyleSheet("""
        border-radius: 20px;
        overflow: hidden;
        background-color: black;
        """)
        """then i set the VidW playing size to fit well in the video container 
        widget it then raises the widget that was previously hidden
        and shows the once hidden widget, and then plays the video"""
        self.VidW.setMinimumSize(QSize(600, 400))
        self.VideoContainer.show()
        self.VideoContainer.raise_()
        self.Vid.play()

    def video2(self) -> None:
        """this function does the same as the video 1 function, it just changes the source video to be something else"""
        self.Vid.setVideoOutput(self.VidW)
        self.Vid.setSource(QUrl.fromLocalFile('ENA.mp4'))
        self.VideoContainer.setStyleSheet("""
        border-radius: 20px;
        overflow: hidden;
        background-color: black;
        """)
        self.VidW.setMinimumSize(QSize(600, 400))
        self.VideoContainer.show()
        self.VideoContainer.raise_()
        self.Vid.play()

    def video3(self) -> None:
        """this function does the same as the video 1 function just with a different video"""
        self.Vid.setVideoOutput(self.VidW)
        self.Vid.setSource(QUrl.fromLocalFile('TRU.mp4'))
        self.VidW.setMinimumSize(QSize(600, 400))
        self.VideoContainer.setStyleSheet("""
        border-radius: 20px;
        overflow: hidden;
        background-color: black;
        """)
        self.VideoContainer.show()
        self.VideoContainer.raise_()
        self.Vid.play()

    def handlemediastatus(self, status: QMediaPlayer.MediaStatus) -> None:
        """this function checks if the status of the Qmedia player has reached the end of the video
        and when the video ends. it goes to the backtovideomenu function where it brings up the video
        choices."""
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.backtovideomenu()

    def backtovideomenu(self) -> None:
        """since i didnt remove the buttons or disable them since the widget ontop prevents the user from interacting
        with it, i just stop the video. then i hide the video container widget and lower it so that the user can
        select the next video"""
        self.Vid.stop()
        self.VideoContainer.hide()
        self.VideoContainer.lower()


    def submit(self) -> None:
        """this submit function just enables the yes or no buttons that dont work unless the submit button is pressed
        first, it then plays a sound effect when pressed and then does a name check, if the name check returns a none,
         then it asks the user for their name and if not then it asks the user to confirm if this is their real name.
         thats where the yes and no buttons come into place."""
        self.Click_sound = QSoundEffect()
        self.Click_sound.setSource(QUrl.fromLocalFile('CLICK.wav'))
        self.Click_sound.setVolume(0.6)
        self.Click_sound.play()
        name = self.namecheck()
        if name == '':
            self.Question.setText("Enter your NAME!!!")
            return
        self.Yes.setDisabled(False)
        self.N.setDisabled(False)
        self.Question.setText("Is this your real name?")





