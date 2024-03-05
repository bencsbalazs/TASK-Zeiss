As a data engineer, you can't expect to always deal with data directly. Requests coming form stakeholders often require a certain level of expertise in programming to fulfill; moreover, the actual task to be undertaken can also be a bit obscure when first encountered.

In this vein, in order to test your mettle, please consider the following scenario:

A researcher has taken upon himself to automate the packaging of heavy lab equipment with a robotic arm. Nevertheless, he forgot to account for the fact that certain pieces of equipment, even when neatly packaged in a box, can only withstand a certain amount of pressure without being damaged for so long.

The boxes stood on top of each other for months without issue, but the time has come for them to be rearranged in order to prevent the stored equipment from getting damaged. Although the researcher who developed the system has already moved on to work on another project and cannot be contacted, he did leave behind everything that's needed for rearranging the boxes:

* a HeavyLifter v1 (the robotic arm itself)
* the app to control it,
* two *instruction set files*, that you can feed into it (one of which we have included as the attachment)
* and a *README.md* file (also included in the attachment)

The only problem is that he forgot to label which instruction set should be fed into the machine first. Feeding the wrong set can irreparably damage the equipment, so you cannot test things out with the real equipment.

Nevertheless, the other researchers can immediately tell you whether an instruction set is the right one, if you tell them which boxes end up on top of each stack.

Your task is to write an application which when given an *instruction set file* as an *input*, can simulate the movement of the arm, so that we know in which order the boxes will end up in.

The expected *output* is a *string consisting of the letters of the boxes sitting on top of each stack* (e.g. considering the example given in the *README.md*, the expected output is: `FPAT`)

Food for thought (don't implement it!):

* How would you design such an application so that it remained usable even when the capabilities of the underlying machine change (e.g. HeavyLifter v2 is used which can move multiple crates at the same time, in which case, considering the example given in the *README.md*, the expected output would be: `BPKT`, or a different input format was expected)
