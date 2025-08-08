import remi.gui as gui
from remi import start, App
from Bio.PDB import PDBParser # Import PDBParser

class MDSetupApp(App):
    def __init__(self, *args, **kwargs):
        # You can configure Remi here, e.g. address='0.0.0.0', port=0
        super(MDSetupApp, self).__init__(*args, **kwargs)

    def main(self):
        # Create a container for the GUI elements
        main_container = gui.VBox(width=500, height=600, margin='0px auto') # Increased height
        main_container.style['justify-content'] = 'center'
        main_container.style['align-items'] = 'center'

        # Add a label
        lbl_title = gui.Label('GROMACS MD System Setup', font_size=20)
        main_container.append(lbl_title)

        # Add a file upload widget
        self.file_upload = gui.FileUploader(width=200, height=30, margin='10px')
        self.file_upload.set_on_file_upload_complete(self.on_file_upload_complete)
        main_container.append(self.file_upload)

        # Force field selection
        lbl_forcefield = gui.Label('Select Force Field:', margin='10px')
        main_container.append(lbl_forcefield)
        self.dropdown_forcefield = gui.DropDown(width=200, height=30, margin='5px')
        self.dropdown_forcefield.append(gui.DropDownItem('CHARMM36m', 'charmm36m')) # Added CHARMM36m option
        # Add more force fields here later if needed
        main_container.append(self.dropdown_forcefield)

        # Solvent selection
        lbl_solvent = gui.Label('Select Solvent:', margin='10px')
        main_container.append(lbl_solvent)
        self.dropdown_solvent = gui.DropDown(width=200, height=30, margin='5px')
        self.dropdown_solvent.append(gui.DropDownItem('TIP3P', 'tip3p'))
        self.dropdown_solvent.append(gui.DropDownItem('TIP4P', 'tip4p'))
        self.dropdown_solvent.append(gui.DropDownItem('SPC/E', 'spce'))
        # Add more solvents here later if needed
        main_container.append(self.dropdown_solvent)

        # Box dimensions input
        lbl_box_dimensions = gui.Label('Enter Box Dimensions (nm):', margin='10px')
        main_container.append(lbl_box_dimensions)

        hbox_box_dimensions = gui.HBox(width=300, height=30, margin='5px')
        self.txt_box_x = gui.TextInput(width=80, height=30, margin='0px 5px 0px 0px', hint='X')
        self.txt_box_y = gui.TextInput(width=80, height=30, margin='0px 5px 0px 0px', hint='Y')
        self.txt_box_z = gui.TextInput(width=80, height=30, margin='0px', hint='Z')
        hbox_box_dimensions.append(self.txt_box_x)
        hbox_box_dimensions.append(self.txt_box_y)
        hbox_box_dimensions.append(self.txt_box_z)
        main_container.append(hbox_box_dimensions)


        # Placeholder for other controls (e.g., box type)
        lbl_options_placeholder = gui.Label('Other options will go here...', margin='10px')
        # main_container.append(lbl_options_placeholder) # Removing placeholder as we added box dimensions

        # Placeholder for a process button
        # We'll add this later
        btn_process = gui.Button('Prepare System', width=150, height=30, margin='10px')
        # btn_process.set_on_click(self.on_process_click) # We'll define this later
        main_container.append(btn_process)

        # Placeholder for output area
        lbl_output_placeholder = gui.Label('Output will be shown here...', margin='10px')
        main_container.append(lbl_output_placeholder)


        # Return the main container
        return main_container

    def on_file_upload_complete(self, widget, filename, filepath):
        # This function is called when a file is uploaded
        print(f"File uploaded: {filename}")
        print(f"File saved to: {filepath}")
        # You can now process the uploaded file from 'filepath' using Biopython

        parser = PDBParser()
        try:
            structure = parser.get_structure('protein', filepath)
            print(f"Successfully parsed PDB file: {filename}")
            # You can now work with the 'structure' object

            # You can also access the selected force field and solvent like this:
            selected_forcefield = self.dropdown_forcefield.get_value()
            selected_solvent = self.dropdown_solvent.get_value()
            box_x = self.txt_box_x.get_value()
            box_y = self.txt_box_y.get_value()
            box_z = self.txt_box_z.get_value()

            print(f"Selected force field: {selected_forcefield}")
            print(f"Selected solvent: {selected_solvent}")
            print(f"Box dimensions: X={box_x}, Y={box_y}, Z={box_z}")


        except Exception as e:
            print(f"Error parsing PDB file: {e}")


# To run the application:
start(MDSetupApp, address='0.0.0.0', port=8081, enable_file_cache=False, debug=True)

