#!/usr/bin/env python3

from app import webapp
import os
import uuid
from werkzeug.utils import secure_filename


class UploadController():
    # Generate unique file ID
    def idGenerator():
        return str(uuid.uuid4())

    # Get file extension
    def getExtension(filename):
        return filename.split('.')[-1]

    # Check for allowed file extension
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower(
               ) in webapp.config['ALLOWED_EXTENSIONS']

    def maxFileSize():
        # Get maximum allowed file size
        fileSize = webapp.config['MAX_CONTENT_LENGTH']
        # Convert to MB
        inMB = fileSize / 1024 / 1024
        return int(inMB)

    # Upload file to upload folder
    def uploadFile(data, user_id):
        if 'itemPicture' in data:
            file = data['itemPicture']

            # if file exist and it's allowed
            if file and UploadController.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # generate random new filename
                # user_id-randomstring.ext
                randomFileName = user_id + '-'
                randomFileName += UploadController.idGenerator() + '.'
                randomFileName += UploadController.getExtension(filename)
                # Save file to configured upload folder
                file.save(os.path.join(
                    webapp.config['UPLOAD_FOLDER'],
                    randomFileName))

                return randomFileName
        else:
            # If no picture is selected submit empty string
            return ''
