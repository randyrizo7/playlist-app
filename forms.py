"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    playlist_name = StringField('Playlist Name', validators=[InputRequired(message='Add playlist name')])
    playlist_description = TextAreaField('Playlist Description', validators=[InputRequired(message='Add a playlist description (ex: workout, summer jams, ect')])


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    song_title = StringField('Song Title', validators=[InputRequired(message='Enter Song Title')])
    song_artist = StringField('Song Artist', validators=[InputRequired(message='Enter Name of Song Artist')])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
