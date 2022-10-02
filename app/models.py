"""
Module that is responsible for creating,
different tables inside our database
"""

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from db_config import Base


class YoutubeTranscript(Base):
    """Class that will create our table"""

    __tablename__ = "youtube_transcripts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    content = Column(String, nullable=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())


# Test model for our YouTube Transcript table:
# class YoutubeTranscriptData(Base):
#     """
#     TEST:
#     Class that will create our Youtube Transcript table
#     """
#
#     __tablename__ = "youtube_transcript_data"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     author = Column(String, nullable=False)
#     transcript = Column(String, nullable=False)
#     start_time_in_seconds = Column(Float, nullable=False)
#     duration_in_seconds = Column(Float, nullable=False)
#     time_created = Column(DateTime(timezone=True), server_default=func.now())
