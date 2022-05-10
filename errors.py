messages = {
    1: { # Invalid number detected.
        1: "The first part of the SSN has an invalid number.",
        2: "The second part of the SSN has an invalid number.",
        3: "The third part of the SSN has an invalid number."
    },

    2: { # Letter detected.
        1: "The first part of the SSN contains letters.",
        2: "The second part of the SSN contains letters.",
        3: "The third part of the SSN contains letters."
    },
    
    3: { # Lack or excess of digits per part detected.
        1: "The first part has an excess or lack of digits.",
        2: "The second part has an excess or lack of digits.",
        3: "The third part has an excess or lack of digits."
    },

    4: { # Bad formatting detected.
        1: "The total amount of parts of the SSN is greater than three.",
        2: "The total amount of parts of the SSN is less than three."
    }
}