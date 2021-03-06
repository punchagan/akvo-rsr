/** @jsx React.DOM */

// Akvo RSR is covered by the GNU Affero General Public License.
// See more details in the license.txt file located at the root folder of the
// Akvo RSR module. For additional details on the GNU license please see
// < http://www.gnu.org/licenses/agpl.html >.

document.addEventListener("DOMContentLoaded", function() {
    var i18n = JSON.parse(document.getElementById("updates-text").innerHTML),
        dropdown_filters = ["location", "organisation", "sector"],
        hidden_or_other = ["title_or_subtitle", "page"],
        url = "/rest/v1/update_directory",
        typeahead_url = "/rest/v1/typeaheads/project_updates?format=json";

    ReactDOM.render(
        <DirectoryApp
            type={"updates"}
            dropdown_filters={dropdown_filters}
            hidden_or_other={hidden_or_other}
            options_url={url}
            i18n={i18n}
            typeahead_url={typeahead_url}
        />,
        document.getElementById("update-directory")
    );
});
