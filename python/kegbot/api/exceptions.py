# Copyright 2014 Mike Wakerly <opensource@hoho.com>
#
# This file is part of the Pykeg package of the Kegbot project.
# For more information on Pykeg or Kegbot, see http://kegbot.org/
#
# Pykeg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Pykeg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pykeg.  If not, see <http://www.gnu.org/licenses/>.

class Error(Exception):
  """An error occurred."""
  HTTP_CODE = 400
  def Message(self):
    if self.message:
      return self.message
    m = self.__class__.__doc__
    m = m.split('\n', 1)[0]
    return m

class NotFoundError(Error):
  """The requested object could not be found."""
  HTTP_CODE = 404

class RequestError(Error):
  """There was an error fufilling the request."""

class ServerError(Error):
  """The server had a problem fulfilling your request."""
  HTTP_CODE = 500

class BadRequestError(Error):
  """The request was incomplete or malformed."""
  HTTP_CODE = 400

class NoAuthTokenError(Error):
  """An api_key is required."""
  HTTP_CODE = 401

class BadApiKeyError(Error):
  """The api_key given is invalid."""
  HTTP_CODE = 401

class PermissionDeniedError(Error):
  """The api_key given does not have permission for this resource."""
  HTTP_CODE = 401

MAP_NAME_TO_EXCEPTION = dict((c.__name__, c) for c in Error.__subclasses__())

def ErrorCodeToException(code, message=ServerError):
  cls = MAP_NAME_TO_EXCEPTION.get(code, Error)
  return cls(message)

