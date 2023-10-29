## DOFAS KITCHEN APP

The DOFAS KITCHEN APP is a Command Line Interface (CLI) application that provides users with the ability to register their details and access various features within the application.

### Features

1. **User Registration:** Register your personal details in the application.
2. **Custom CLI Commands:** Perform various tasks using intuitive command-line commands.
3. **Access Data:** Retrieve and interact with user and menu data.
4. **Database Management:** Manage user profiles, menus, and restaurant information.
5. **Interconnected Data:** Users, menus, and restaurants are interconnected for a comprehensive experience.

### Installation

1. Clone the repository: `git clone https://github.com/YourGitHubUsername/DOFAS-KITCHEN-APP.git`
2. Navigate to the DOFAS KITCHEN APP directory: `cd DOFAS-KITCHEN-APP`
3. Run the installation script: `./install.sh`

### Getting Started

1. Open your terminal.
2. Type `dofas-kitchen` to launch the DOFAS KITCHEN APP.

### Commands

- `add-user [first_name] [last_name] [email] [phone_number]`: Add a new user to the database.
- `add-menu [breakfast] [lunch] [dinner] [ethnic]`: Add a new menu to the database.
- `add-restaurant [soft_drink] [alcoholic_drink] [wine] [user_id] [menu_id]`: Add a new restaurant to the database.
- `list-users-menus-restaurants`: List all users, their menus, and corresponding restaurants.

### Examples

- Add a new user: `dofas-kitchen add-user "Mary" "Francis" "john@example.com" 1234567890`
- Add a new menu: `dofas-kitchen add-menu "Pancakes" "Burger" "Pizza" "Italian"`
- Add a new restaurant: `dofas-kitchen add-restaurant "Coke" "Wine" "RedWine" 1 2`
- List users, menus, and restaurants: `dofas-kitchen list-users-menus-restaurants`

### Configuration

- Configuration settings for the DOFAS KITCHEN APP can be customized using the `config` command.

### Feedback

Your feedback is important to us! If you encounter any issues or have suggestions for improvement, please visit our GitHub repository [https://github.com/YourGitHubUsername/DOFAS-KITCHEN-APP] to open an issue.

Thank you for using the DOFAS KITCHEN APP! Enjoy exploring the world of food and users!

---

