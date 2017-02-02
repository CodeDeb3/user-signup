#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

def build_page():

    content= """<html><head>
        <style>
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
    <h1>Signup</h1>
        <form method="post">
            <table>
                <tbody><tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="" required="">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password" required="">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password" required="">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" type="email" value="">
                        <span class="error"></span>
                    </td>
                </tr>
            </tbody></table>
            <input type="submit">
        </form>

</body></html>"""

    # name_label = "<label>Name </label>"
    # name_input = "<input type ='number' name='rotation'/>"
    #
    # message_label = "<label class='blah'> Type a message: </label>"
    # textarea = "<textarea name='message'>" + textarea_content + "</textarea>"
    #
    # submit = "<input type='submit' value='Submit'/>"
    # form = ("<form method='post'>" +
    #         rotate_label + rotation_input + "<br>" +
    #         message_label + textarea + "<br>" +
    #         submit + "</form>")
    #
    # header = "<h2> Web Caesar</h2>"

    return content


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #header



        self.response.write(build_page())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
