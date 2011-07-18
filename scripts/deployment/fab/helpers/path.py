# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


class Path(object):

    def __init__(self, fabric_runner, permissions_helper, feedback):
        self.fabric = fabric_runner
        self.permissions = permissions_helper
        self.feedback = feedback

    def ensure_path_exists_with_akvo_group_permissions(self, path):
        if self.fabric.path_exists(path):
            self.feedback.comment(">> Found expected path: %s" % path)
        else:
            self._ensure_path_exists_with(path, self.fabric.sudo)
            self.permissions.set_akvo_group_permissions_on_path(path)

    def ensure_path_exists(self, path):
        self._ensure_path_exists_with(path, self.fabric.run)

    def ensure_path_exists_with_sudo(self, path):
        self._ensure_path_exists_with(path, self.fabric.sudo)

    def _ensure_path_exists_with(self, path, run_command):
        if self.fabric.path_exists(path):
            self.feedback.comment(">> Found expected path: %s" % path)
        else:
            self.feedback.comment(">> Creating path: %s" % path)
            run_command("mkdir %s" % path)
            run_command("chmod 755 %s" % path)

    def exit_if_path_does_not_exist(self, path):
        if not self.fabric.path_exists(path):
            self.feedback.abort("\n>> Expected path does not exist: %s" % path)
